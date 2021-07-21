class Computer:
    def __init__(self, type_of_os, storage_capacity, ram_size):
        self.type_of_os = type_of_os
        self.storage_capacity = storage_capacity
        self.ram_size = ram_size
    def playGame(self, nameOfGame):
        print("The computer is playing ", nameOfGame)

asus = Computer("Window","1GB","4GB-RAM")
print(asus.type_of_os)
print(asus.storage_capacity)
print(asus.ram_size)
asus.playGame('Among Us')

class Laptop(Computer):
    def __init__(self, storage_capacity, ram_size):
        Computer.__init__(self, 'Mac', storage_capacity, ram_size)

Mac = Laptop('2GB',"6GB-RAM")
print(Mac.type_of_os)
print(Mac.storage_capacity)
print(Mac.ram_size)
Mac.playGame('Roblox')

class Desktop(Computer):
    def __init__(self, storage_capacity, ram_size):
        Computer.__init__(self, 'Window', storage_capacity, ram_size)

hp = Desktop('3GB',"2GB-RAM")
print(hp.type_of_os)
print(hp.storage_capacity)
print(hp.ram_size)
hp.playGame('Candy Crush')