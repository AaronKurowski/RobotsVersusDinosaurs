import random

class Dinosaur:
    def __init__(self, type, energy, attack_power):
        self.type = type
        self.health = 100
        self.energy = energy
        self.attack_power = attack_power
        #self.crushing_blow_chance = 0

    def display_dino_attributes(self):
        print("\nDino type: " + self.type)
        print("Current health: " + str(self.health))
        print("Energy level: " + str(self.energy))
        print("Attack power: " + str(self.attack_power))
        # print("Attack power: " + str(self.weapon_ap))

    def set_name(self):
        self.type = input("What type of dino?")

    def set_energy(self):
        # self.energy = random.randomint(5, 25)
        pass

        def set_type(self):
            self.type = input('Choose a dinosaur: (raptor/stegosaurus/t-rex)')
            if self.type == "raptor":
                self.health = 75
                self.energy = 120
                self.attack_power = 10
                # self.crushing_blow_chance = .19
            elif self.type == "stegosaurus":
                self.health = 125
                self.energy = 90
                self.attack_power = 25
                # self.crushing_blow_chance = .4
            elif self.type == "t-rex":
                self.health = 100
                self.energy = 150
                self.attack_power = 19
                # self.crushing_blow_chance = .5