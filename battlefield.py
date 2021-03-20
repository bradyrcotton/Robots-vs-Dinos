from fleet import Fleet
from herd import Herd
import random


class Battlefield:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def attack_sequence(self, attacker, defender):
        defender.health -= attacker.attack
        print(f"{attacker.type} attacks {defender.type}")
        attacker.health -= defender.attack
        print(f"{defender.type} attacks {attacker.type}")

    def run_game(self):

        def get_random_number():
            random_int = random_number(0, 2)
            return random_int
        i = get_random_number()
        j = 0
        k = 0

        while i < 3:

            while self.herd.herd[i].health > 0 and self.fleet.fleet[i].health > 0:
                self.attack_sequence(self.herd.herd[i], self.fleet.fleet[i])
                if self.herd.herd[i].health > 0:
                    print(f"{self.herd.herd[i].type}'s HP = {self.herd.herd[i].health}")
                if self.fleet.fleet[i].health > 0:
                    print(f"{self.fleet.fleet[i].type}'s HP = {self.fleet.fleet[i].health}")

            if self.herd.herd[i].health <= 0:
                print(f"{self.herd.herd[i].type} is dead")
                i += 1
                j += 1

            elif self.fleet.fleet[i].health <= 0:
                print(f"{self.fleet.fleet[i].type} is dead")
                i += 1
                k += 1

        if i >= 3:
            if j > k:
                print("The fleet of robots has destroyed the herd of dinosaurs")
            else:
                print("The herd of dinosaurs has defeated the fleet of robots")


def random_number(min_value, max_value):

    return random.randint(min_value, max_value)


Battlefield().run_game()

