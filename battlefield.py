class Battlefield:
    from dino import Dino
    from robot import Robot

    robot_one = Robot("OP", 100, 15)
    robot_two = Robot("BB", 100, 20)
    robot_three = Robot("DC", 100, 20)

    dino_one = Dino("Raptor", 100, 15)
    dino_two = Dino("T-rex", 1500, 10)
    dino_three = Dino("Stegosauras", 1000, 5)

    while robot_one.robos_health > 0 and dino_one.dinos_health > 0:
        Dino.dino_attack(dino_one, robot_one)
        Robot.robot_attack(robot_one, dino_one)
        if robot_one.robos_health > 0:
            print(robot_one.robos_health)
        if dino_one.dinos_health > 0:
            print(dino_one.dinos_health)
        elif robot_one.robos_health < 0:
            print(f"{robot_one.robos_type} is dead")
        elif dino_one.dinos_health < 0:
            print(f"{dino_one.dinos_type} is dead")
