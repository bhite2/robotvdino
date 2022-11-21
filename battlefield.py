from dino import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Bender")
        self.dinosaur = Dinosaur()
        pass
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robot vs. Dinosaur")
        print("Who will reign supreme? Past or Future?")

    def battle_phase(self):
        # I will need a loop that stops at which character gets to zero first
        self.robot.attack(self.dinosaur)
        pass

    def display_winner(self):
        pass
