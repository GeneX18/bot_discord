import random

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

    def gainExp(self, n):
        max = (self.lvl ^ 5 + 50)
        self.exp += n
        if self.exp >= max:
            self.exp -= max
            self.changeLvl(1)

    def printInfo(self):
        info = self.nome + ": " + self.classe + " lvl " + str(
            self.lvl) + "\nHealth stat:" + str(
                self.health) + "\nPower stat:" + str(self.power)
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
        return 20
    
    def fight(self):
        pg_actionTxt = self.pg.nome+""
        en_actionTxt = self.enemy.nome+""
        hit = random.randint(1,20)
        dmg = random.randint(2,12)+self.pg.power
        if hit == 1:
            #miss
            pg_actionTxt += " manca il bersaglio"
            dmg = 0
        elif hit == 20:
            #crit
            pg_actionTxt += " devasta il bersaglio"
            dmg += 12
        else:
            #hit
            pg_actionTxt += " colpisce il bersaglio"
            
        pg_actionTxt += " infliggendo "+ str(dmg) +" danni"
        self.enemy_hp -= dmg
        if self.enemy_hp <= 0:
            pg_actionTxt += " uccidendo il bersaglio.\nHAI VINTO!"
            return pg_actionTxt
        pg_actionTxt += ".\n"
        
        hit = random.randint(1,20)
        dmg = random.randint(2,8)
        
        if hit == 1:
            #miss
            en_actionTxt += " manca il bersaglio"
            dmg = 0
        elif hit >= 18:
            #crit
            en_actionTxt += " devasta il bersaglio"
            dmg += 8
        else:
            #hit
            en_actionTxt += " colpisce il bersaglio"
        en_actionTxt += " infliggendo "+ str(dmg) +" danni"
        self.enemy_hp -= dmg
        if self.enemy_hp <= 0:
            en_actionTxt += " uccidendo il bersaglio.\nHAI PERSO!"
        else:
            en_actionTxt += "."
        return pg_actionTxt+en_actionTxt