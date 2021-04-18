from robot import Robot
from herd import Herd
from dinosaur import Dinosaur
from weapon import Weapon
from fleet import Fleet
from battlefield import Battlefield

if __name__ == '__main__':
    battlefield = Battlefield()
    battlefield.display_welcome()
    user_start = input("\nStart game? (yes/no) >")
    if user_start == 'yes':
        battlefield.run_game()

    else:
        print("Exiting 3..2..1..")
