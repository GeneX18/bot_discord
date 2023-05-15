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