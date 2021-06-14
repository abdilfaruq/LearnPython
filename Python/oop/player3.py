"""
class Player:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    #//classmethod && staticmethod

player = Player('Dybala')
print(player.getName())
"""

class Player:
    job = 'pemain bola'
    
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @staticmethod
    def retiredIn(age):
        return str(40 - age)

    @classmethod
    #def generalInfo(cls):
    #    return cls.job + ' akan pensiun dalam 40 tahun'
    def generalInfo(cls, age):
        return cls.job + ' ini akan pensiun dalam '+ cls.retiredIn(age) + ' tahun'

print(Player.generalInfo(30))