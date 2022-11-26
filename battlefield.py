from dino import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Bender")
        self.dinosaur = Dinosaur("Barney")
        
    def run_game(self):
        self.display_welcome()
        print("")
        self.battle_phase()
        print("")
        self.display_winner()

    def display_welcome(self):
        print("Ladies and gentlemen. Welcome to the main event of the evening!")
        print("This is Robot vs. Dinosaur")
        print("A battle, millions of years in the making")
        print("To the thousands in attendance, and the millions watching at home")
        print("Let's get Ready to Rumbleeeeeeeeeeee!")

    def battle_phase(self):
        # I will need a loop that stops at which character gets to zero first
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)

            elif self.robot.health <= 0:
                print(f"{self.robot.name} is down and knocked out.")

            if self.dinosaur.health > 0:
                self.dinosaur.attack_robot(self.robot)
            
            elif self.dinosaur.health <= 0:
                print(f"{self.dinosaur.name} is down and knocked out.")

            
    def display_winner(self):
        print("We have a winner")
        if self.robot.health > 0:
            print("Robot wins!!!!!!")

        else:
            print("Dinosaur wins!!!!!!")


