# importation de la fonction randint, du module random
from random import randint


class Character:
    def __init__(self, name, life, strength, defense, weapon, magic_scroll):
        self.name = name
        self.life = life
        self.strength = strength
        self.defense = defense
        self.weapon = weapon
        self.magic_scroll = magic_scroll

    def attack(self, target):
        # Détermination des dégâts faits par l'assaillant
        strike = self.weapon.hit()
        # Détermination des dégâts évités par le défenseur
        protect = target.weapon.parade()
        # Calcul des dégâts finalement reçus
        wound = strike - protect
        wound = max(0, wound)
        # Mise-à-jour des points de vie du défenseur
        target.life = target.life - wound
        # Textes descriptifs dans la console
        if strike == 0:
            print(f"{self.name} a raté sa cible.")
        else:
            print(self.name, "a attaqué", target.name)
            print(target.name, "encaisse", protect, "pts grâce à sa parade.")
            print(target.name, "reçoit", wound, "pts de dégât.")
        print(target.name, "a encore", target.life, "pts de vie.")

    def healing(self):
        # Détermination des points de vie récupérés
        cure = self.magic_scroll.read_scroll()
        # Mise-à-jour des points de vie
        self.life += cure
        # Textes descriptifs dans la console
        print(self.name, "se soigne et récupère", cure, "points de vie.")

    def description(self):
        print(
            f"Name: {self.name} ; HP: {self.life} ; Weapon: {self.weapon.__dict__} ; Magic Scroll : {self.magic_scroll.__dict__}\n")


"""
INSTANCIATION DES CLASSES
"""

# instanciation des objets de classe Character


class Weapon:
    def __init__(self, name, damage, protection, accuracy):
        self.name = name
        self.damage = damage
        self.protection = protection
        self.accuracy = accuracy

    def hit(self):
        hit_damage = 0
        if randint(0, 100) < self.accuracy:
            hit_damage = randint(1, self.damage)
        return hit_damage

    def parade(self):
        parade_defense = randint(1, self.protection)
        return parade_defense


class Magic_Scroll:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def read_scroll(self):
        effect = randint(1, self.power)
        return effect


"""
ALGORITHME PRINCIPAL
"""

weapons_att = [
    {
        "name": "Rusty Sword",
        "damage": 5,
        "protection": 1,
        "accuracy": 60
    },
    {
        "name": "Wooden Axe",
        "damage": 2,
        "protection": 1,
        "accuracy": 42
    },
    {
        "name": "Iron Sword",
        "damage": 7,
        "protection": 3,
        "accuracy": 65
    },
    {
        "name": "Bow",
        "damage": 4,
        "protection": 1,
        "accuracy": 50
    },
]


weapon_menu = True
weapons = [Weapon(**w) for w in weapons_att]
weapon_chosen = None

while weapon_menu:

    print("Choose your weapon soldier: ")
    for i in range(len(weapons)):
        print(f"[{i}]: {weapons[i].__dict__}")

    try:
        choice = int(input("Choice: [0, 1, 2, ...]"))
        if choice < 0 or choice > len(weapons):
            continue

        weapon_chosen = weapons[choice]
        weapon_menu = False
        print(f"You have chosen: {weapon_chosen.__dict__}")
    except ValueError as e:
        print(e)


ms_att = [
    {
        "name": "Health",
        "power": 5
    }
]
ms = [Magic_Scroll(**m) for m in ms_att]
ms_chosen = None

ms_menu = True


while ms_menu:
    print("Choose your magic scroll soldier: ")
    for i in range(len(ms)):
        print(f"[{i}]: {ms[i].__dict__}")

    try:
        choice = int(input("Choice: [0, 1, 2, ...]"))
        if choice < 0 or choice > len(ms):
            continue

        ms_chosen = ms[choice]
        ms_menu = False
        print(f"You have chosen: {ms_chosen.__dict__}")
    except ValueError as e:
        print(e)


player = Character("Nairod", 12, 6, 2, weapon_chosen, ms_chosen)
opponent = Character("Keguli", 12, 7, 1, Weapon(
    "Axe", 3, 1, 64), Magic_Scroll("Poison", 1))


# Initialisation du compteur de tours de combat
fight_round = 1
# Boucle du combat
player.description()
opponent.description()
while player.life > 0 and opponent.life > 0:
    print("-------------------------------------")
    print("TOUR ", fight_round)
    print("-------------------------------------")
    print(player.name, ":", player.life, "PV //",
          opponent.name, ":", opponent.life, "PV")
    print("-------------------------------------")
    # Gestion de l'action du joueur
    print("------ ", player.name, " ------")
    action = int(input("Que voulez-vous faire? (attaque 1, récupération 2)"))
    if action == 1:
        player.attack(opponent)
    elif action == 2:
        player.healing()
    # Gestion de l'action de l'ennemi
    print("------ ", opponent.name, " ------")
    if opponent.life > 5:
        opponent.attack(player)
    else:
        opponent.healing()
    # Incrémentation du compteur de tour de combat
    fight_round += 1
    print()
# Gestion de la fin du combat
print("-------------------------------------------")
print("-------------- FIN DU COMBAT --------------")
print("-------------------------------------------")
if player.life <= 0:
    print(player.name, "est KO")
if opponent.life <= 0:
    print(opponent.name, "est KO")
