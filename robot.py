from weapon import Weapon

class Robot:
    def __init__(self, name, power_level, weapon):
        self.name = name
        self.health = 100
        self.power_level = power_level
        self.weapon = weapon

    def set_attributes(self):
        pass

    def set_name(self):
        # self.name = input("\nName your robot >")
        pass

    def choose_weapon(self):
        # self.weapon.pick_weapon()
        pass

    def display_robot_attributes(self):
        print("\nRobot name: " + self.name)
        print("Current health: " + str(self.health))
        print("Power level: " + str(self.power_level))
        print("Weapon: " + self.weapon.type + " --> AP: " + str(self.weapon.attack_power))
        # print("Attack power: " + str(self.weapon_ap))