class Weapon:
    def __init__(self):
        self.weapon_type = ''
        self.attack_power = 0
        #self.accuracy = 0
        #self.critical_chance = 0

    def pick_weapon(self):
        self.weapon_type = input("Choose a weapon: sword/mace/axe >")
        if self.weapon_type == "sword":
            self.attack_power = 12
            #self.critical_chance = .35
            #self.accuracy = 0.9
        elif self.weapon_type == "mace":
            self.attack_power = 25
            #self.critical_chance = .20
            #self.accuracy = 0.7
        elif self.weapon_type == "axe":
            self.attack_power = 20
            #self.critical_chance = .27
            #self.accuracy = .8

    def display_weapon_attributes(self):
        print("Weapon type: " + self.weapon_type)
        print("Weapon attack power: " + str(self.attack_power))
