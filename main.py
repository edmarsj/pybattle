from random import seed
from dotdict import dotdict
from hero import *
from skills import add_skills
from game import Game

# seed random number generator
seed(1)

hero = Hero()
hero.name = ""
hero.hp = 20
hero.atk = 5
hero.deff = 3
hero.kills = 0
hero.maxhp = 20
hero.kills_level_up = 2
hero.level = 1

monster = dotdict({
    'name': "Goblin",
    'hp': 6,
    'atk': 2,
    'deff': 1,
    'level': 1
})

add_skills(hero, monster)

clear()
print('Wellcome hero! What is your name?')
hero.name = input()
clear()
print(
    f"Thats a really brave name sir {hero.name}! Lets begin our journey shall we?")

game = Game(hero, monster)

game.game_loop()
