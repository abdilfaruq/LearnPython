class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def infoPlayer(self):
        return self.name + ' adalah ' + self.age

    @infoPlayer.setter
    def infoPlayer(self, data):
        name, age = data.split(' ')
        self.name = name
        self.age = age

player = Player('Dybala', '23')
player.infoPlayer = 'PauloDybala 24'
print(player.infoPlayer)