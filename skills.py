from hero import Skill

def add_skills(hero, monster):

    hero.skills = {
        1: Skill(
            hero,
            'Atack',
            0,
            1,
            (lambda: hero.attack(hero.atk, monster))),

        2: Skill(
            hero,
            'Heal',
            0,
            1,
            (lambda: hero.heal())),

        3: Skill(
            hero,
            'Charged Attack',
            1,
            2,
            (lambda: hero.attack(hero.atk + 5, monster)))
    }
