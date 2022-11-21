from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("flamethrower", 40)
    
    def attack(self, dinosaur):
        dino.health -= self.weapon.attack_power