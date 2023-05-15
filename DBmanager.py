import pickle

db_char = {}
db_combat = {}

class DBmanager:
    def __init__(self, f_name):
        self.f_name = f_name
        print(f_name)

    #Upload
    def loadFromFile(self):
        global db_char
        try:
            with open(self.f_name, 'rb') as f:
                
                db_char = pickle.load(f)
        except EOFError:
                db_char = {}
    #Save
    def saveInFile(self):
        with open(self.f_name, 'wb') as f:
            pickle.dump(db_char, f)

    #Characters DB Methods
    def getDB(self):
        return db_char

    def dictFromDB(self, id):
        return db_char[id].__dict__

    def getKeys(self):
        return db_char.keys()

    def updateDB(self, id, obj):
        db_char[id] = obj

    def deleteDB(self, id):
        del db_char[id]
        self.saveInFile()
        
    #Combats DB Methods
    def isInCombat(self, usrId):
        if usrId in db_combat.keys():
            return True
        else:
            return False
        
    def getCombatInfo(self, usrId):
        return db_combat[usrId]
    
    def endCombat(self, usrId):
        del db_combat[usrId]
