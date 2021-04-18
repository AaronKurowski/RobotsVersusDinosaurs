import random

class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 100
        self.attack_power = attack_power
        #self.crushing_blow_chance = 0

    def attack_robot(self, robot):
        robot.health -= 10

    def display_dino_attributes(self):
        print("\nDino type: " + self.type)
        print("Current health: " + str(self.health))
        print("Energy level: " + str(self.energy))
        print("Attack power: " + str(self.attack_power))
        # print("Attack power: " + str(self.weapon_ap))
