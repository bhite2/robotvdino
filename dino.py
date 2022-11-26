class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        
    def attack_robot(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name} for {self.attack_power} damage. {robot.name} new health is {robot.health}.")