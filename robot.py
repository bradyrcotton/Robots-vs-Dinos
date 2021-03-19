class Robot:

    def __init__(self, robot, power, attack):
        self.robos_type = robot
        self.robos_health = 100
        self.robos_power = power
        self.robos_attack = attack

    def robot_attack(self, dino):
        dino.dinos_health -= self.robos_attack
