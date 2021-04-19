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
        # self.bot_fleet.show_bot_team()
        self.battle()
        self.display_winners()

    def battle(self):
        battle_active = True
        while battle_active:
            self.first_turn = True
            while self.first_turn:
                user_attack = input("\nAttack with which robot? (Type options to display attackable dinosaurs!)"
                                    "\n1 = Jenny, 2 = Bipbop, 3 = Gooblium)"
                                    "\n >")
                if user_attack == 'options':
                    self.show_dino_opponent_options()
                    continue
                elif user_attack == '1':
                    if self.bot_fleet.fleet[0].power_level > 0:
                        self.robot_turn(self.bot_fleet.fleet[0])
                        break
                    else:
                        print("No more power!")
                        continue
                elif user_attack == '2':
                    if self.dino_herd.herd[1].power_level > 0:
                        self.robot_turn(self.bot_fleet.fleet[1])
                        break
                    else:
                        print("No more power!")
                        continue
                elif user_attack == '3':
                    if self.bot_fleet.fleet[0].power_level > 0:
                        self.robot_turn(self.bot_fleet.fleet[2])
                        break
                    else:
                        continue
                if self.display_winners():
                    battle_active = False
                    break
                # self.first_turn = False
            self.second_turn = True
            while self.second_turn:
                user_attack = input("\nAttack with which dino? (Type options to display attackable robots!)"
                                    "\n1 = Raptor, 2 = T-Rex, 3 = Stegosaurus"
                                    "\n >")
                if user_attack == 'options':
                    self.bot_fleet.show_bot_team()
                    continue
                elif user_attack == '1':
                    if self.dino_herd.herd[0].energy != 0:
                        self.dino_turn(self.dino_herd.herd[0])
                    else:
                        print("This dino is all out of energy!")
                        continue
                elif user_attack == '2':
                    if self.dino_herd.herd[1].energy != 0:
                        self.dino_turn(self.dino_herd.herd[1])
                    else:
                        print("This dino is all out of energy!")
                        continue
                elif user_attack == '3':
                    if self.dino_herd.herd[2].energy != 0:
                        self.dino_turn(self.dino_herd.herd[2])
                    else:
                        print("This dino is all out of energy!")
                        continue

                if self.display_winners():
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
        self.choose_dino_victim = input("Choose a dino to attack! \n (1 = Raptor, 2 = T-Rex, 3 = Stegosaurus) >")
        if self.choose_dino_victim == '1':
            robot.attack_dino(self.dino_herd.herd[0])
            robot.power_level -= 10
            print("\n<=======|==o__ATTACK__o==|=======>")
            print("" + robot.name + " attacks " + self.dino_herd.herd[0].type + " for " +
                  str(robot.weapon.attack_power) + "! \n" + "Robot energy decreases by 10!")
            print("<=======|==o__ATTACK__o==|=======>")
            self.dino_herd.herd[0].display_dino_attributes()
        elif self.choose_dino_victim == '2':
            robot.attack_dino(self.dino_herd.herd[1])
            robot.power_level -= 10
            print("\n<=======|==o__ATTACK__o==|=======>")
            print("" + robot.name + " attacks " + self.dino_herd.herd[1].type + " for " +
                  str(robot.weapon.attack_power) + "! \n" + "Robot energy decreases by 10!")
            print("<=======|==o__ATTACK__o==|=======>")
            self.dino_herd.herd[1].display_dino_attributes()
        elif self.choose_dino_victim == '3':
            robot.attack_dino(self.dino_herd.herd[2])
            robot.power_level -= 10
            print("\n<=======|==o__ATTACK__o==|=======>")
            print("" + robot.name + " attacks " + self.dino_herd.herd[2].type + " for " +
                  str(robot.weapon.attack_power) + "! \n" + "Robot  energy decreases by 10!")
            print("<=======|==o__ATTACK__o==|=======>")
            self.dino_herd.herd[2].display_dino_attributes()
        else:
            self.robot_turn(robot)

    def dino_turn(self, dinosaur):
        # make robot opponent pickable
        self.choose_bot_victim = input("\nAttack which bot? \n (1 = Jenny, 2 = Bipbop, 3 = Gooblium)"
                                       "\n >")
        if self.choose_bot_victim == '1':
            dinosaur.attack_robot(self.bot_fleet.fleet[0])
            dinosaur.energy -= 10
            print("\n<=======|==o__ATTACK__o==|=======>")
            print("" + dinosaur.type + " attacks " + self.bot_fleet.fleet[0].name + " for " +
                  str(dinosaur.attack_power) + "!\n" + "Her energy decreases by 10!")
            print("<=======|==o__ATTACK__o==|=======>")
            self.bot_fleet.fleet[0].display_robot_attributes()
        elif self.choose_bot_victim == '2':
            dinosaur.attack_robot(self.bot_fleet.fleet[1])
            dinosaur.energy -= 10
            print("\n<=======|==o__ATTACK__o==|=======>")
            print("" + dinosaur.type + " attacks " + self.bot_fleet.fleet[0].name + " for " +
                  str(dinosaur.attack_power) + "!\n" + "Her energy decreases by 10!")
            print("<=======|==o__ATTACK__o==|=======>")
            self.bot_fleet.fleet[1].display_robot_attributes()
        else:
            dinosaur.attack_robot(self.bot_fleet.fleet[2])
            dinosaur.energy -= 10
            print("\n<=======|==o__ATTACK__o==|=======>")
            print("" + dinosaur.type + " attacks " + self.bot_fleet.fleet[0].name + " for " +
                  str(dinosaur.attack_power) + "!\n" + "Her energy decreases by 10!")
            print("<=======|==o__ATTACK__o==|=======>")
            self.bot_fleet.fleet[2].display_robot_attributes()

    def show_dino_opponent_options(self):
        # show all dinos that are attackable
        self.dino_herd.show_dino_herd()

    def show_robot_opponent_options(self):
        # show all attackable robots
        self.bot_fleet.show_bot_team()

    def display_winners(self):
        if self.dino_herd.herd[0].health <= 0 and self.dino_herd.herd[1].health <= 0 and self.dino_herd.herd[2].health <= 0:
            print("\nROBOTS WIN")
            return True
        elif self.bot_fleet.fleet[0].health <= 0 and self.bot_fleet.fleet[1].health <= 0 and self.bot_fleet.fleet[2].health <= 0:
            print("\nDINOSAURS WIN")
            return True
        else:
            return False
