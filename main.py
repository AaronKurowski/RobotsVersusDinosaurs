from robot import Robot
from herd import Herd
from dinosaur import Dinosaur
from weapon import Weapon
from fleet import Fleet
from battlefield import Battlefield

if __name__ == '__main__':
    # instantiate robots and fleet
    # robot1 = Robot("Jenny", 90, Weapon("Sword", 34.4))
    # robot2 = Robot("Bipbop", 125, Weapon("Axe", 25))
    # robot3 = Robot("Gooblium", 110, Weapon("Dagger", 31))

    # robot_fleet = Fleet()
    # robot_fleet.create_robots()
    # print(robot_fleet.create_robots)
    # print(robot_fleet.fleet[0].name)

    # start of game
    print("Welcome to robots VS dinosaurs!")
    start_game = input("Play? (yes/no) >")
    if start_game.lower() == 'yes':
        print("* * * * * * * * * * * * * * * * * * * * ")
        print("---------------------------------------")
        print("               COMMENCE")
        print("---------------------------------------")
        print("* * * * * * * * * * * * * * * * * * * * ")
        user_team = input("Robot or Dinosaur? >")
        if user_team.lower() == 'robot':
            user_robot_fleet = Fleet()
            user_robot_fleet.create_robots()
            user_robot_fleet.show_bot_team()

            print("\nCreating enemy dinosaurs...3...2..1..")
            cpu_dino_herd = Herd()
            cpu_dino_herd.create_dinosaurs()
            cpu_dino_herd.show_dino_herd()







        elif user_team.lower() == 'dinosaur':
            dino_herd = Herd()
            # # user = Robot()
            # cpu = Dinosaur(50)
            # #user.set_name()
            # cpu.set_name()
            # cpu.display_dino_attributes()

            print("\ngot here!")
            input("exit?")




            # robot_fleet = Fleet()
            # robot_fleet.create_robots()
            # dino_herd = Herd()
            # dino_herd.create_dinosaurs()
    else:
        print("Exiting 3..2..1..")


    # #instantiate dinos
    # dino_one = Dinosaur()
    # dino_one.set_type()
    #
    # dino_two = Dinosaur()
    # dino_two.set_type()
    #
    # dino_three = Dinosaur()
    # dino_three.set_type()


