from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.power_level = 12.5
        self.weapon = ''

    def set_name(self):
        self.name = input("Name your robot >")

    def choose_weapon(self):
        robot_weapon = Weapon()
        robot_weapon.pick_weapon()
        self.weapon = robot_weapon.weapon_type

    def display_robot_attributes(self):
        print("Robot name: " + self.name)
        print("Current health: " + str(self.health))
        print("Power level: " + str(self.power_level))
        print("Weapon of choice: " + self.weapon)