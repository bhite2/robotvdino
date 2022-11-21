from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = "Bender"
        self.health = 100
        self.weapon = Weapon("flamethrower", 40)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage. {dinosaur.name} remaining health is {dinosaur.health}.")