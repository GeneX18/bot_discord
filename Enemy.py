import random
import math
from Ability import Ability

#[minValue, maxValue]
dices = [[1,6], [2,8], [2,12], [3,12], [4,16], [3,18]]

class Enemy:
    def __init__(self, nome, gs, abilities = []):
        self.nome = nome
        self.gs = gs
        self.abilities = abilities
        
        if self.hasAbility(Ability.BUTCHER):
            self.critVal = 16
        else:
            self.critVal = 19
        
        self.dmg_dices = dices[gs]
        
        self.STR_mod = gs
        if self.hasAbility(Ability.STRONG):
            self.STR_mod += 3
            
        
    def hasAbility(self, ab):
        if ab in self.abilities: return True
        return False

    def giveExp(self):
        val : float = 5.0+(5.5*self.gs)
        return math.ceil(val*10)/10
    
    def fight(self, combat):
        isFightOver = False
        en_actionTxt = self.nome+""
        
        hit = random.randint(1,20)
        dmg = random.randint(self.dmg_dices[0],self.dmg_dices[1])+self.STR_mod
        
        if hit == 1:
            #miss
            en_actionTxt += " manca il bersaglio"
            dmg = 0
        elif hit >= self.critVal:
            #crit
            en_actionTxt += " infligge un colpo devastante"
            dmg += self.dmg_dices[1]
        else:
            #hit
            en_actionTxt += " colpisce"
        en_actionTxt += " infliggendo "+ str(dmg) +" danni"
        combat.pg_hp -= dmg
        if combat.pg_hp <= 0:
            isFightOver = True
            en_actionTxt += " uccidendo il bersaglio.\nHAI PERSO!"
            combat.pg.loseExp()
        else:
            en_actionTxt += "."
            
        return [isFightOver, en_actionTxt]
