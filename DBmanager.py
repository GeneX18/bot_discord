import pickle

dbmap = {}


class DBmanager:
    def __init__(self, f_name):
        self.f_name = f_name
        print(f_name)

    def loadFromFile(self):
        try:
            with open(self.f_name, 'rb') as f:
                global dbmap
                dbmap = pickle.load(f)
        except EOFError:
                dbmap = {}

    def saveInFile(self):
        with open(self.f_name, 'wb') as f:
            pickle.dump(dbmap, f)

    def getDB(self):
        return dbmap

    def dictFromDB(self, id):
        return dbmap[id].__dict__

    def getKeys(self):
        return dbmap.keys()

    def updateDB(self, id, obj):
        dbmap[id] = obj

    def deleteDB(self, id):
        del dbmap[id]
        self.saveInFile()
