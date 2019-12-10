from utils import clear

class Game:
    hero = {}
    monster = {}

    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster

    # Fight sequence
    def fight(self):

        skills = self.hero.enabled_skills()

        while True:
            print("\nWhat do you wanna do?")

            for action in skills:
                if skills[action].enabled():
                    print(f"{action} - {skills[action].name}")

            choice = input()

            if choice.isdigit() and int(choice) in skills:
                break
            else:
                print("This option is not available at this moment")

        clear()
        skills[int(choice)].execute()

        if self.monster.hp < 1:
            self.hero.kills += 1
            print(
                f"You defeated {self.monster.name}! You killed {self.hero.kills} monsters today! ({self.hero.kills_level_up - self.hero.kills} left to level up)")
            if self.hero.kills == self.hero.kills_level_up:
                self.hero.level_up()
                clear()

            self.monster.respawn()
        else:
            self.monster.attack(self.hero)

    # Main game loop
    def game_loop(self):
        print(
            f"A blood thirsty {self.monster.name} has appeared in front of you!")

        while self.hero.hp > 0:
            print(f"\n\nHP: {self.hero.hp}/{self.hero.max_hp}")
            print(f"Energy: {self.hero.energy}/{self.hero.max_energy}")
            self.fight()
