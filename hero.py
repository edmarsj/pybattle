from utils import *


class Skill:
    def __init__(self, hero, pname, pcooldown, pmin_level, pfunction):
        self.hero = hero
        self.name = pname
        self.cooldown = pcooldown + 1
        self.cooldown_counter = 0
        self.min_level = pmin_level
        self._function = pfunction

    def execute(self):
        self.cooldown_counter = self.cooldown
        self._function()

    def step(self):
        if self.cooldown_counter > 0:
            self.cooldown_counter -= 1

    def enabled(self):
        return self.hero.level >= self.min_level and self.cooldown_counter == 0


class Hero:

    skills = {}

    def attack(self, atk, monster):
        damage = calculate_damage(atk, monster.deff)

        if damage > 0:
            print(
                f"You attacked {monster.name} causing {damage} points of damage")
            monster.hp -= damage
        else:
            print(f"You missed!")

    def heal(self):
        heal = 5
        for x in range(self.level):
            heal += roll_dice(6)

        if (heal + self.hp) > self.maxhp:
            heal = self.maxhp - self.hp

        self.hp += heal

        print(f"You healled {heal} life points")

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

        print(f"\n\nYou are now at level {self.level}. And has been fully healed!")
        points = self.level + 3
        while points > 0:
            print(f"\n\nYou have {points} points left to spend!")
            print("What stats would you like to improve?")
            print("1 - Attack")
            print("2 - Defence")
            print("3 - Life")

            choice = int(input())
            if choice == 1:
                print('You grew up even stronger!')
                self.atk += 1
            elif choice == 2:
                print('You grew up even harder to beat!')
                self.deff += 1
            else:
                print(
                    "I told you you would become a lot healthier eating all those vegetables haven't I?")
                self.maxhp += 1

            points -= 1

        self.hp = self.maxhp

    def enabled_skills(self):
        # dict comprehension is bizarre!
        return {k: v for (k, v) in self.skills.items() if v.enabled()}

    def refresh_skills(self):
        for skill in self.skills:
            self.skills[skill].step()
