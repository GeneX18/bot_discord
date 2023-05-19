import random
from Enemy import Enemy
from Ability import Ability

#Enemies
cinghiale = Enemy("Cinghiale",0)
coniglio_mannaro = Enemy("Coniglio mannaro",1,[Ability.SUPER_SPEED])
goblin = Enemy("Goblin",1,[Ability.COWARD])
bugbear = Enemy("Bugbear",2)
orsogufo = Enemy("Orsogufo",2)
treant = Enemy("Treant",3)
drago_verde = Enemy("Drago verde",5,[Ability.SUPER_SPEED,Ability.BUTCHER])
ragno = Enemy("Ragno gigante",1)
bandito = Enemy("Bandito",1,[Ability.COWARD])
proto_nero = Enemy("Protoplasma nero",2)
orco = Enemy("Orco",3,[Ability.BUTCHER])
golem_pietra = Enemy("Golem di Pietra",4,[Ability.BUTCHER])



loc = ["Foresta Lunare", "Cave Rosse"]
spawnList = [[
    cinghiale, coniglio_mannaro, goblin, orsogufo, treant,
    drago_verde
],
             [
                 ragno, bandito, bugbear, proto_nero,
                 orco, golem_pietra
             ]]
spawnRate = [.4, .2, .2, .15, .04, .01]


class Map:
    def locationList(self):
        msg = ""
        for number, l in enumerate(loc):
            msg += str(number + 1) + "] " + l + "\n"
        return msg

    def canExplore(self, locId):
        lID = locId - 1
        if lID < 0 or lID >= len(loc):
            return False
        return True

    def locationName(self, locId):
        lID = locId - 1
        return loc[lID]

    def explore(self, locId):
        lID = locId - 1
        list = spawnList[lID]
        encounter = random.choices(list, spawnRate, k=1)[0]
        print(encounter)

        return encounter
