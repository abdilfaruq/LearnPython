class Player:

    def __init__(self, name):
        self.name = name
        #self.__age = 23
        self.__age = '23'

    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

class ArgentinaPlayer(Player):
    pass

player = ArgentinaPlayer('Dybala')
player._Player__age = '25'
#player.name = 'Dybala JR'
print(player.getAge() + " - " + player.getName())