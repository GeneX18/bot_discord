import random
import math
from Ability import Ability

class PG:
    def __init__(self, nome, classe, lvl, exp, health, power):
        self.nome = nome
        self.classe = classe
        self.lvl = lvl
        self.exp = exp
        self.health = health
        self.power = power

    def changeLvl(self, n):
        if(self.lvl == 5):
            return
        self.lvl += n

    def maxExpFormula(self):
        return math.ceil((88*(1.3**(self.lvl-1)))*10)/10
    
    
    def gainExp(self, n):
        max : float = self.maxExpFormula()
        self.exp += n
        if self.exp >= max:
            self.exp -= max
            self.changeLvl(1)
            
    def loseExp(self):
        self.exp = 0.0

    def fight(self, combat):
        pg_actionTxt = self.nome+""
        
        hit = random.randint(1,20)
        
        #PARRY
        if combat.enemy.hasAbility(Ability.PARRY):
            if (hit < 6):
                hit = 0
                g_actionTxt += combat.enemy.nome+" para il colpo in arrivo.\n"


        dmg = random.randint(2,12)+self.power
        if hit == 1:
            #miss
            pg_actionTxt += " manca il bersaglio"
            dmg = 0
        elif hit == 20:
            #crit
            pg_actionTxt += " infligge un colpo devastante"
            dmg += 12
        else:
            #hit
            pg_actionTxt += " colpisce"
            
        pg_actionTxt += " infliggendo "+ str(dmg) +" danni"
        combat.enemy_hp -= dmg
        if combat.enemy_hp <= 0:
            pg_actionTxt += " uccidendo il bersaglio.\nHAI VINTO!"
            self.gainExp(combat.enemy.giveExp())
            return [True, pg_actionTxt]
        
        pg_actionTxt += "."
        return [False, pg_actionTxt]
        
        
        
    def printInfo(self):
        info = self.nome + ": " + self.classe + " lvl " + str(
            self.lvl) + "\nExp [" + str(self.exp) + "/" + str(self.maxExpFormula()) + "]" + "\nHealth stat: " + str(
                self.health) + "\nPower stat: " + str(self.power)
        return info

def getPGinfo(obj):
    return PG(obj['nome'], obj['classe'], obj['lvl'], obj['exp'],
              obj['health'], obj['power'])


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError("Unserializable object {} of type {}".format(
            obj, type(obj)))





class Combat:
    def __init__(self, pg, enemy, round = 0):
        self.pg = pg
        self.enemy = enemy
        self.pg_hp = self.getMaxPgHp()
        self.enemy_hp = self.getMaxEnemyHp()
        self.round = round
        
    def getMaxPgHp(self):
        return 20+((5+self.pg.health)*self.pg.lvl)
    
    def getMaxEnemyHp(self):
        return 15+(9*self.enemy.gs)
    
    def fight(self):
        isFightOver = False
        
        final_txt = ""
        
        self.round += 1
        if self.round == 1:
            if self.enemy.hasAbility(Ability.DISTANCE):
                enemyResult = self.enemy.fight(self)
                final_txt += self.enemy.nome+" vede il bersaglio dalla distanza e ne approfitta!\n"
                final_txt += enemyResult[1]+"\n"
                isFightOver = enemyResult[0]
                return [isFightOver,final_txt]
        
        if self.enemy.hasAbility(Ability.SUPER_SPEED):
            enemyResult = self.enemy.fight(self)
            if enemyResult[0]:
                return enemyResult
            final_txt += enemyResult[1]+"\n"
            
            pgResult = self.pg.fight(self)
            final_txt += pgResult[1]
            isFightOver = pgResult[0]
            
        else:
            pgResult = self.pg.fight(self)
            if pgResult[0]:
                return pgResult
            final_txt += pgResult[1]+"\n"
            
            enemyResult = self.enemy.fight(self)
            final_txt += enemyResult[1]
            isFightOver = enemyResult[0]
            
        if self.enemy.hasAbility(Ability.COWARD):
            if((self.enemy_hp*2)<self.getMaxEnemyHp()):
                return [True, final_txt + "\n"+self.enemy.nome+" fugge spaventato."]
        
        return [isFightOver, final_txt]