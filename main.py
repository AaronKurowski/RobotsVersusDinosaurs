from robot import Robot
from dinosaur import Dinosaur

if __name__ == '__main__':
    # instantiate robots
    robot_one = Robot()
    robot_one.set_name()
    robot_one.choose_weapon()

    robot_two = Robot()
    robot_two.set_name()
    robot_two.choose_weapon()

    robot_three = Robot()
    robot_three.set_name()
    robot_three.choose_weapon()

    robot_one.display_robot_attributes()
    robot_two.display_robot_attributes()
    robot_three.display_robot_attributes()

    #instantiate dinos
    dino_one = Dinosaur()
    dino_one.set_type()

    dino_two = Dinosaur()
    dino_two.set_type()

    dino_three = Dinosaur()
    dino_three.set_type()


