from random import seed
from hero import *
from skills import add_skills
from game import Game
from monster import Monster

# seed random number generator
seed(1)

hero = Hero()
hero.name = ""
hero.hp = 20
hero.atk = 5
hero.deff = 3
hero.kills = 0
hero.max_hp = 20
hero.energy = 3
hero.max_energy = 3
hero.kills_level_up = 2
hero.level = 1

monster = Monster()
monster.name = "Goblin"
monster.hp = 6
monster.atk = 2
monster.deff = 1
monster.level = 1


add_skills(hero, monster)
hero.skills[0]=Skill(
    hero,
    'Quit',
    0,
    0,
    (lambda: exit()))

clear()
print('Wellcome hero! What is your name?')
hero.name = input()
clear()
print(
    f"Thats a really brave name sir {hero.name}! Lets begin our journey shall we?\n\n\n")

game = Game(hero, monster)

game.game_loop()
