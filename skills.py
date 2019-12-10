from hero import Skill
from utils import roll_dice


def add_skills(hero, monster):

    hero.skills = {

        # Basic attack
        1: Skill(
            hero,
            name='Atack',
            energy=0,
            min_level=1,
            action=(lambda: hero.attack(hero.atk, monster))),

        # Heals 1d8 life points per level
        2: Skill(
            hero,
            name='Heal (1)',
            energy=1,
            min_level=1,
            action=(lambda: hero.heal())),

        # A stronger attack +5
        3: Skill(
            hero,
            name='Charged Attack (1)',
            energy=1,
            min_level=2,
            action=(lambda: hero.attack(hero.atk + 5, monster))),

        # Adds another dice roll to the charged attack
        4: Skill(
            hero,
            name='Double tap (2)',
            energy=2,
            min_level=3,
            action=(lambda: hero.attack(hero.atk + 5 + roll_dice(8), monster)))
    }
