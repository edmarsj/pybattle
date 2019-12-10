from utils import *


# Skills used by the hero
class Skill:
    def __init__(self, hero, name, energy, min_level, action):
        self.hero = hero
        self.name = name
        self.energy = energy
        self.min_level = min_level
        self._action = action

    # Executes the action and decreases the hero energy
    def execute(self):
        self.hero.energy -= self.energy
        self._action()

    # Skills can only be enabled if the minimum level was achieved and if the hero still has enough energy
    def enabled(self):
        return self.hero.level >= self.min_level and self.hero.energy >= self.energy


class Hero:

    skills = {}

    # Attacks a moster
    def attack(self, atk, monster):
        damage = calculate_damage(atk, monster.deff)

        if damage > 0:
            print(
                f"You attacked {monster.name} causing {damage} points of damage")
            monster.hp -= damage
        else:
            print(f"You missed!")

    # Heal
    def heal(self):
        heal = 5
        for x in range(self.level):
            heal += roll_dice(6)

        if (heal + self.hp) > self.max_hp:
            heal = self.max_hp - self.hp

        self.hp += heal

        print(f"You healled {heal} life points")

    # Level up the hero - allow the player to choose which stats to improove
    def level_up(self):
        self.level += 1
        self.kills_level_up += self.level + 1

        # check for new skills
        new_skills = {k: v for (k, v) in self.skills.items()
                      if v.min_level == self.level}
        if len(new_skills) > 0:
            print(f'\nCongratulations! You have a new skill:')
            for skill in new_skills:
                print(new_skills[skill].name)

        print(
            f"\n\nYou are now at level {self.level}. And has been fully healed and your energy has been fully retored!")
        points = self.level + 3
        while points > 0:
            print(f"\n\nYou have {points} points left to spend!")
            print("What stats would you like to improve?")
            print("1 - Attack")
            print("2 - Defence")
            print("3 - Life")
            print("4 - Energy")

            choice = int(input())
            if choice == 1:
                print('You grew up even stronger!')
                self.atk += 1
            elif choice == 2:
                print('You grew up even harder to beat!')
                self.deff += 1
            elif choice == 3:
                print(
                    "I told you you would become a lot healthier eating all those vegetables haven't I?")
                self.max_hp += 1
            elif choice == 4:
                print(
                    "I told you you would become a lot more energetic eating all those vegetables haven't I?")
                self.max_energy += 1
            else:
                print('Option not available.')
                continue

            points -= 1

        self.hp = self.max_hp
        self.energy = self.max_energy

    # Filters out disabled skills
    def enabled_skills(self):
        # dict comprehension is bizarre!
        return {k: v for (k, v) in self.skills.items() if v.enabled()}
