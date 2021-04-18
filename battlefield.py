from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.bot_fleet = Fleet()
        self.dino_herd = Herd()
        self.bot_fleet.create_robots()
        self.dino_herd.create_dinosaurs()

    def run_game(self):
        self.commence()
        self.bot_fleet.show_bot_team()
        self.battle()
        self.display_winners()

    def battle(self):
        battle_active = True
        self.second_turn = True
        self.first_turn = True
        while battle_active:
            while self.first_turn:
                user_attack = input("\nAttack with which robot?"
                                    "\n1 = Jenny, 2 = Bipbop, 3 = Gooblium"
                                    "\n >")
                if user_attack == '1':
                    self.robot_turn(self.bot_fleet.fleet[0])
                elif user_attack == '2':
                    self.robot_turn(self.bot_fleet.fleet[1])
                elif user_attack == '3':
                    self.robot_turn(self.bot_fleet.fleet[2])

                if self.dino_herd.herd[0].health <= 0 and self.dino_herd.herd[1].health <= 0 and \
                        self.dino_herd.herd[2].health <= 0:
                    battle_active = False
                    break
                break
            while self.second_turn:
                user_attack = input("\nAttack with which dino?"
                                    "\n1 = Raptor, 2 = T-Rex, 3 = Stegosaurus"
                                    "\n >")
                if user_attack == '1':
                    self.dino_turn(self.dino_herd.herd[0])
                elif user_attack == '2':
                    self.dino_turn(self.dino_herd.herd[1])
                elif user_attack == '3':
                    self.dino_turn(self.dino_herd.herd[2])

                if self.bot_fleet.fleet[0].health == 0 and self.bot_fleet.fleet[1].health == 0 and \
                        self.bot_fleet.fleet[2] == 0:
                    battle_active = False
                    break
                break

    def first_strike(self):
        user_team = input("Who goes first. Bots or Dinos? >")
        if user_team == 'bots':
            self.robot_turn(self.bot_fleet.fleet[0])
        elif user_team == 'dinos':
            self.dino_turn(self.dino_herd.herd[0])

    def display_welcome(self):
        print("Welcome to Robots VS Dinosaurs")

    def commence(self):
        print("* * * * * * * * * * * * * * * * * * * * ")
        print("---------------------------------------")
        print("               COMMENCE")
        print("---------------------------------------")
        print("* * * * * * * * * * * * * * * * * * * * ")

    def robot_turn(self, robot):
        # make this able to pick which to attack
        self.choose_victim = input("Attack which dino? \n (1=raptor/2=t-rex/3=stegosaurus) >")
        if self.choose_victim == '1':
            robot.attack_dino(self.dino_herd.herd[0])
            self.dino_herd.herd[0].display_dino_attributes()
        elif self.choose_victim == '2':
            robot.attack_dino(self.dino_herd.herd[1])
            self.dino_herd.herd[1].display_dino_attributes()
        else:
            robot.attack_dino(self.dino_herd.herd[2])
            self.dino_herd.herd[2].display_dino_attributes()

    def dino_turn(self, dinosaur):
        # make robot opponent pickable
        self.choose_victim = input("Attack which bot? \n (1=Jenny, 2=Bipbop, 3=Gooblium")
        if self.choose_victim == '1':
            dinosaur.attack_robot(self.bot_fleet.fleet[0])
            self.bot_fleet.fleet[0].display_robot_attributes()
        elif self.choose_victim == '2':
            dinosaur.attack_robot(self.bot_fleet.fleet[1])
            self.bot_fleet.fleet[1].display_robot_attributes()
        else:
            dinosaur.attack_robot(self.bot_fleet.fleet[2])
            self.bot_fleet.fleet[2].display_robot_attributes()

    def show_dino_opponent_options(self):
        # show all dinos that are attackable
        pass

    def show_robot_opponent_options(self):
        # show all attackable robots
        pass

    def display_winners(self):
        print("robots WIN")
