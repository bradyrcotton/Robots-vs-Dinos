from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def attack_sequence(self, attacker, defender):
        defender.health -= attacker.attack
        # print(defender.health)

    def run_game(self):

        i = 0
        while i <= 3:
            self.attack_sequence(self.herd.herd[i], self.fleet.fleet[i] )
            if i <= 3:

                while self.herd.herd[i].health > 0 and self.fleet.fleet[i].health > 0:
                    self.attack_sequence(self.herd.herd[i], self.fleet.fleet[i])
                    if self.herd.herd[i].health > 0:
                        print(self.herd.herd[i].health)
                    if self.fleet.fleet[i].health > 0:
                        print(self.fleet.fleet[i].health)

                if self.herd.herd[i].health <= 0:
                    print(f"{self.herd.herd[i].type} is dead")
                    i += 1
                elif self.fleet.fleet[i].health <= 0:
                    print(f"{self.fleet.fleet[i].type} is dead")
                    i += 1
Battlefield().run_game()


    # print(Herd.herd[0])

    # while robot_one.robos_health > 0 and dino_one.dinos_health > 0:
    #     Dino.dino_attack(dino_one, robot_one)
    #     Robot.robot_attack(robot_one, dino_one)
    #     if robot_one.robos_health > 0:
    #         print(robot_one.robos_health)
    #     if dino_one.dinos_health > 0:
    #         print(dino_one.dinos_health)
    #     elif robot_one.robos_health < 0:
    #         print(f"{robot_one.robos_type} is dead")
    #     elif dino_one.dinos_health < 0:
    #         print(f"{dino_one.dinos_type} is dead")
