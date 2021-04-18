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
        self.battle()
        self.display_welcome()

    def battle(self):
        game_bool = True
        self.second_turn = True
        self.first_turn = True
        while game_bool:
            while self.first_turn:
                user_attack = input("Press 1 to attack as robot!")
                if user_attack == '1':
                    self.robot_turn(self.bot_fleet.fleet[0])
                    self.dino_herd.show_dino_herd()
                    break
                if self.dino_herd.herd[0].health == 0:
                    game_bool = False
                    break
                break
            while self.second_turn:
                if game_bool == False:
                    break
                self.dino_turn(self.dino_herd.herd[0])
                if self.dino_herd.herd[0].health == 0:
                    game_bool = False
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
        robot.attack_dino(self.dino_herd.herd[0])
        # if self.dino_herd.herd[0].health == 0:
        #     robot.attack_dino(self.dino_herd.herd[1])
        # elif self.dino_herd.herd[0].health == 0 and self.dino_herd.herd[1].health == 0:
        #     robot.attack_dino(self.dino_herd.herd[2])

    def dino_turn(self, dinosaur):
        dinosaur.attack_robot(self.bot_fleet.fleet[0])

    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass

        # print(self.bot_fleet[0].type + " will attack " + self.dino_herd[0].type)
        # self.dino_herd[0].health -= 10
        # print(self.bot_fleet[0].name + " hit " + self.dino_herd[0].name + " for 10!")

        # display welcome
        # self.display_welcome()
        # let user choose who goes first

        # actual battle rounds
        # choose a dino
        # choose a robot
        #repeat until one side dies

        #display winner