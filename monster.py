from utils import *
from random import randint

monster_names = [
    "Goblin",
    "Dragon",
    "White Walker",
    "Walker (Zoombie)",
    "Snake",
    "Hydra",
    "Hell hound",
    "Fairy dust vampire",
    "Random commit message"
]


class Monster:

    # Monster attacks the hero
    def attack(self, hero):
        damage = calculate_damage(self.atk, hero.deff)

        if damage > 0:
            print(f"{self.name} attacked you causing {damage} points of damage")
            hero.hp -= damage
        else:
            print(f"{self.name} missed!")

        if hero.hp < 1:
            print(
                f"You were defeated, but the world will always remember you for killing {hero.kills} monsters this day.")
            exit()

    # Monster respawn
    def respawn(self):
        self.name = monster_names[randint(0, len(monster_names)-1)]
        self.level += 1
        self.atk += randint(0, 2)
        self.deff += 1
        self.hp = self.level * 4
        
        print(f"\n\nA very strong looking {self.name} appeared!")
