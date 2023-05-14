import random

loc = ["Foresta Lunare", "Cave Rosse"]
spawnList = [[
    "Cinghiale", "Coniglio Mannaro", "Goblin", "Orsogufo", "Treant",
    "Drago verde"
],
             [
                 "Ragno gigante", "Bandito", "Bugbear", "Protoplasma nero",
                 "Orco", "Golem di Pietra"
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
        encounter = ''.join(random.choices(list, spawnRate, k=1))

        return encounter
