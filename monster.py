from utils import *

def monster_attack(monster, hero):
    damage = calculate_damage(monster.atk, hero.deff)

    if damage > 0:
        print(f"{monster.name} attacked you causing {damage} points of damage")
        hero.hp -= damage
    else:
        print(f"{monster.name} missed!")

    if hero.hp < 1:
        print(
            f"You were defeated, but the world will always remember you for killing {hero.kills} monsters this day.")
        exit()


def new_monster(monster):
    print(f"\n\nAn even more strong {monster.name} appeared!")
    monster.level += 1
    monster.atk += randint(0, 2)
    monster.deff += 1
    monster.hp = monster.level * 4
