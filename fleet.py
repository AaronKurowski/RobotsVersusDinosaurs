from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.fleet = []
        self.armory = [Weapon("Mace", 19), Weapon("Axe", 24), Weapon("Sword", 33.4)]
        self.create_robots()

    def create_robots(self):
        robot1 = Robot("Jenny")
        robot2 = Robot("Bipbop")
        robot3 = Robot("Gooblium")

        # append these to fleet
        self.fleet.append(robot1)
        self.fleet.append(robot2)
        self.fleet.append(robot3)

    def show_bot_team(self):
        print("\nYour team is: ")
        self.fleet[0].display_robot_attributes()
        self.fleet[1].display_robot_attributes()
        self.fleet[2].display_robot_attributes()