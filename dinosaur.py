class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = 0
        self.energy = 0
        self.attack_power = 0
        #self.crushing_blow_chance = 0

    def set_type(self):
        self.type = input('Choose a dinosaur: (raptor/stegosaurus/t-rex')
        if self.type == "raptor":
            self.health = 75
            self.energy = 120
            self.attack_power = 10
            #self.crushing_blow_chance = .19
        elif self.type == "stegosaurus":
            self.health = 125
            self.energy = 90
            self.attack_power = 25
            #self.crushing_blow_chance = .4
        elif self.type == "t-rex":
            self.health = 100
            self.energy = 150
            self.attack_power = 19
            #self.crushing_blow_chance = .5

    def display_dino_attributes(self):
        print("Dino type: " + self.type)
        print("Health: " + self.type)
        print("Energy: " + self.type)
        print("Attack power: " + self.type)