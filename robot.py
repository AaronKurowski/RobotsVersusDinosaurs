from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        # self.weapon = Weapon()
        # self.crit_chance = crit_chance

    def attack_dino(self, dinosaur):
        dinosaur.health -= 100

    def display_robot_attributes(self):
        print("       Name: " + self.name)
        print("     Health: " + str(self.health))
        print("Power level: " + str(self.power_level))
        # print("Weapon: " + self.weapon.type + " --> AP: " + str(self.weapon.attack_power))
        # print("Attack power: " + str(self.weapon_ap))