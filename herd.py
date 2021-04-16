from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.herd = []

    def create_dinosaurs(self):
        dino1 = Dinosaur("Raptor", 100, 24)
        dino2 = Dinosaur("T-rex", 100, 34)
        dino3 = Dinosaur("Stegosaurus", 100, 35)

        self.herd.append(dino1)
        self.herd.append(dino2)
        self.herd.append(dino3)

    def show_dino_herd(self):
        self.herd[0].display_dino_attributes()
        self.herd[1].display_dino_attributes()
        self.herd[2].display_dino_attributes()