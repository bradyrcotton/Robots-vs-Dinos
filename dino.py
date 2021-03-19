class Dino:
    def __init__(self, dino, power, attack):
        self.dinos_type = dino
        self.dinos_health = 100
        self.dinos_power = power
        self.dinos_attack = attack

    def dino_attack(self, robot):
        robot.robos_health -= self.dinos_attack


    # def battle(self):
    #     if self.type != "":
    #         self.type = "Raptor"
    #         self.health = 100
    #         self.power = 283
    #         self.attack = 100
    #     elif self.type != "":
    #         self.type = "T-Rex"
    #         self.health = 1000
    #         self.power = 892
    #         self.attack = 1000
    #     elif self.type != "":
    #         self.type = "Stegosaurus"
    #         self.health = 2000
    #         self.power = 100
    #         self.attack = 560




