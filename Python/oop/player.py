"""
OOP - Object Oriented Programming

Class dan Object
"""

"""
class Player:
    name = 'Mbappe'

    def getName(self):
        return self.name

#di luar kelas
pemain = Player()
print(pemain.getName())
"""

"""
class Player:
    name = ''

    def getName(self, name):
        self.name = name
        return self.name

#di luar kelas
pemain = Player()
print(pemain.getName('Griezmann'))
"""

"""
class Player:
    #name = ''
    #speed = ''

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

player = Player('Dybala', '86')
player2 = Player('Messi', '93')
print(player.getName() + " punya speed " + player.getSpeed())
print(player2.getName() + " punya speed " + player2.getSpeed())
"""

"""
class Player:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

class ArgentinaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age


class BrazilPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age

player = ArgentinaPlayer('Dybala', '86')
player2 = BrazilPlayer('Neymar', '86')

#print(player.getName() + " umurnya " + player.setAge('23'))
print(player2.getName() + " umurnya " + player2.setAge('40'))
"""

"""
class Player:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getSkill(self):
        return 'normal'

class ArgentinaPlayer(Player):
    def getSkill(self):
        return 'cepat'


class BrazilPlayer(Player):
    def getSkill(self):
        return 'samba'

class IndonesiaPlayer(Player):
    pass

player = ArgentinaPlayer('Dybala', '86')
print(player.getName() + " skillnya " + player.getSkill())

player3 = IndonesiaPlayer('Sultan', '86')
print(player3.getName() + " skillnya " + player3.getSkill())
"""

class Player:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getSkill(self):
        return 'normal'

class ArgentinaPlayer(Player):
    def __init__(self, name):
        #Player.__init__(self, name)
        super().__init__(name)
        print('Helo Argentina!')

    def getSkill(self):
        return 'cepat'

player = ArgentinaPlayer('Dybala')
print(player.getName() + " skillnya " + player.getSkill())