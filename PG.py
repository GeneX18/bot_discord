import random
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
        self.lvl += n

    def maxExpFormula(self):
        return (88*(1.2^(self.lvl-1)))
    def gainExp(self, n):
        max = self.maxExpFormula()
        self.exp += n
        if self.exp >= max:
            self.exp -= max
            self.changeLvl(1)

    def fight(self, combat):
        pg_actionTxt = self.pg.nome+""
        
        hit = random.randint(1,20)
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
            return [True, pg_actionTxt]
        
        pg_actionTxt += ".\n"
        return [False, pg_actionTxt]
        
        
        
    def printInfo(self):
        info = self.nome + ": " + self.classe + " lvl " + str(
            self.lvl) + "\nExp [" + self.exp + "/" + self.maxExpFormula() + "]" + "\nHealth stat: " + str(
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
    def __init__(self, pg, enemy):
        self.pg = pg
        self.enemy = enemy
        self.pg_hp = self.getMaxPgHp()
        self.enemy_hp = self.getMaxEnemyHp()
        
    def getMaxPgHp(self):
        return 20+((5+self.pg.health)*self.pg.lvl)
    
    def getMaxEnemyHp(self):
        return 15+(9*self.enemy.gs)
    
    def fight(self):
        isFightOver = False
        pg_actionTxt = ""
        en_actionTxt = ""
        
        
        if self.enemy.hasAbility(Ability.COWARD):
            if((self.enemy_hp*3)<self.getMaxEnemyHp()):
                return [True, self.enemy.nome+" fugge spaventato."]
        
        
        if self.enemy.hasAbility(Ability.SUPER_SPEED):
            enemyResult = self.enemy.fight(self)
            if enemyResult[0]:
                return enemyResult
            en_actionTxt = enemyResult[1]
            
            pgResult = self.pg.fight(self)
            pg_actionTxt = pgResult[1]
            isFightOver = pgResult[0]
            
        else:
            pgResult = self.pg.fight(self)
            if pgResult[0]:
                return pgResult
            pg_actionTxt = pgResult[1]
            
            enemyResult = self.enemy.fight(self)
            en_actionTxt = enemyResult[1]
            isFightOver = enemyResult[0]
        
        return [isFightOver, pg_actionTxt+en_actionTxt]