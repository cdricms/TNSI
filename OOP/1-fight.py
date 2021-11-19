import random


class Character():

    name = ""
    hp_total = 10
    is_dead = False
    defend_pts = 0

    def __init__(self, name: str, hp_total: int = 10):
        self.name = name
        self.hp_total = hp_total
        self.defend_pts = random.randrange(3)

    def attack(self, opponent, damage_given: int):
        opponent.hp_total -= opponent.defend(damage_given)
        if opponent.hp_total <= 0:
            opponent.is_dead = True

        return opponent

    def defend(self, damage_given):
        damage_taken = damage_given - self.defend_pts
        if damage_taken > 0:
            return damage_taken

        return 0

    def heal(self):
        if self.hp_total < 10:
            self.hp_total += 1

        self.is_dead = False


def chars_choice():
    creating = True
    while creating:
        name = str(input("Choose the character's name: "))
        if len(name) > 0:
            creating = False

    return Character(name)


def attack(my_char, opponent):
    char_attack(my_char, opponent)
    print("---")

    opponents_choice = random.choice(["attack", "heal"])

    if opponents_choice == "attack":
        char_attack(opponent, my_char)
    else:
        char_heal(opponent)


def char_heal(char: Character):
    print(f"{char.name} heals itself and gains 1 HP")
    char.heal()


def char_attack(char: Character, opponent: Character):
    print(f"{char.name} has attacked {opponent.name}")
    damage_given = random.randrange(5)
    char.attack(opponent, damage_given)
    print(f"{opponent.name} has blocked {opponent.defend_pts} damage points.")
    print(f"{opponent.name} has received {damage_given} damage points.")
    print(f"{opponent.name} has only {opponent.hp_total} left.")


def heal(my_char, opponent):
    char_heal(my_char)
    print("---")
    opponents_choice = random.choice(["attack", "heal"])

    if opponents_choice == "attack":
        char_attack(opponent, my_char)
    else:
        char_heal(opponent)


def main():
    print("Create your character: ")
    my_char = chars_choice()
    print("Create your opponent: ")
    opponent = chars_choice()

    game_on = True

    while game_on:
        a_or_h = int(
            input("Do you want to attack your opponent or heal ? (1, 2)"))

        if a_or_h < 0 or a_or_h > 2:
            print("Please input 1 or Two")
            continue

        if a_or_h == 1:
            attack(my_char, opponent)
        elif a_or_h == 2:
            heal(my_char, opponent)

        if my_char.is_dead or opponent.is_dead:
            game_on = False
            print("Game over.")


if __name__ == "__main__":
    main()
