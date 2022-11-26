from dino import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Bender")
        self.dinosaur = Dinosaur("Barney")
        
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Ladies and gentlemen. Welcome to the main event of the evening!")
        print("This is Robot vs. Dinosaur")
        print("A battle, millions of years in the making")
        print("To the thousands in attendance, and the millions watching at home")
        print("Let's get Ready to Rumbleeeeeeeeeeee!")

    def battle_phase(self):
        # I will need a loop that stops at which character gets to zero first
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack_robot(self.robot)
    

    def display_winner(self):
        pass
