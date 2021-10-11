# 2
perso_a = {'nom': 'Ada', 'age': 15, 'force': 99}
perso_b = {'nom': 'Alan', 'age': 17, 'force': 98}
perso_c = {'nom': 'Grace', 'age': 24, 'force': 95}
perso_d = {'nom': 'Claude', 'age': 23, 'force': 97}


def plus_fort(first_per: dict, sec_per: dict):
    return first_per["nom"] if first_per["force"] > sec_per["force"] else sec_per["nom"]


assert plus_fort(perso_a, perso_b) == 'Ada'
assert plus_fort(perso_b, perso_d) == 'Alan'
assert plus_fort(perso_c, perso_d) == 'Claude'
assert plus_fort(perso_a, perso_b) == 'Ada'
assert plus_fort(perso_b, perso_d) == 'Alan'
assert plus_fort(perso_c, perso_d) == 'Claude'


# 3


def conv_dict(victories: list, names: list):
    dic = {}
    names = sorted(names)
    for name in names:
        dic[name] = 0

    for victory in victories:
        dic[victory] += 1

    print(dic)

    return dic


liste_vic = ['Cléa', 'Cléa', 'Aïcha', 'Dounia']
amies = ["Aïcha", "Cléa", "Béa", "Dounia", "Ella"]

print(conv_dict(liste_vic, amies))

liste_vic = ['Cléa', 'Cléa', 'Aïcha', 'Dounia']
assert conv_dict(liste_vic, amies) == {'Aïcha': 1, 'Béa': 0, 'Cléa': 2, 'Dounia': 1,
                                       'Ella': 0}
liste_vic = ['Ella', 'Ella', 'Béa', 'Cléa', 'Aïcha', 'Aïcha', 'Dounia', 'Ella',
             'Aïcha', 'Dounia']
assert conv_dict(liste_vic, amies) == {'Aïcha': 3, 'Béa': 1, 'Cléa': 1, 'Dounia': 2,
                                       'Ella': 3}
liste_vic = ['Ella', 'Ella', 'Béa', 'Cléa', 'Aïcha', 'Aïcha', 'Dounia', 'Ella',
             'Aïcha', 'Dounia']
assert conv_dict(liste_vic, amies) == {'Aïcha': 3, 'Béa': 1, 'Cléa': 1, 'Dounia': 2,
                                       'Ella': 3}
liste_vic = ['Cléa', 'Aïcha', 'Dounia', 'Béa', 'Béa', 'Béa', 'Cléa', 'Béa', 'Cléa',
             'Cléa', 'Cléa', 'Aïcha', 'Aïcha', 'Dounia', 'Ella', 'Aïcha', 'Dounia', 'Cléa', 'Cléa',
             'Aïcha', 'Béa', 'Dounia', 'Aïcha', 'Ella', 'Ella']
assert conv_dict(liste_vic, amies) == {'Aïcha': 6, 'Béa': 5, 'Cléa': 7, 'Dounia': 4,
                                       'Ella': 3}
liste_vic = ['Aïcha', 'Cléa', 'Dounia', 'Cléa', 'Cléa', 'Béa', 'Dounia', 'Béa',
             'Cléa', 'Dounia', 'Dounia', 'Béa', 'Aïcha', 'Ella', 'Dounia', 'Aïcha', 'Ella', 'Béa',
             'Cléa', 'Dounia', 'Aïcha', 'Aïcha', 'Dounia', 'Cléa', 'Ella', 'Aïcha', 'Dounia',
             'Cléa', 'Béa', 'Cléa', 'Cléa', 'Ella', 'Dounia', 'Aïcha', 'Béa', 'Aïcha', 'Cléa',
             'Aïcha', 'Dounia', 'Béa', 'Ella', 'Aïcha', 'Béa', 'Dounia', 'Ella', 'Dounia', 'Cléa',

             'Béa', 'Aïcha', 'Béa', 'Béa', 'Dounia', 'Cléa', 'Béa', 'Dounia', 'Aïcha', 'Dounia',
             'Ella', 'Aïcha', 'Béa', 'Ella', 'Béa', 'Ella', 'Dounia', 'Ella', 'Cléa', 'Ella',
             'Béa', 'Aïcha', 'Cléa', 'Dounia', 'Ella', 'Ella', 'Ella', 'Béa', 'Béa', 'Dounia',
             'Cléa', 'Dounia', 'Aïcha', 'Béa', 'Dounia', 'Ella', 'Dounia', 'Béa', 'Ella', 'Ella',
             'Dounia', 'Aïcha', 'Ella', 'Dounia', 'Dounia', 'Béa', 'Ella', 'Cléa', 'Cléa',
             'Dounia', 'Ella', 'Ella', 'Cléa', 'Aïcha', 'Béa', 'Ella', 'Béa', 'Cléa', 'Béa',
             'Aïcha', 'Ella', 'Aïcha', 'Cléa', 'Dounia', 'Cléa', 'Béa', 'Ella', 'Ella', 'Ella',
             'Aïcha', 'Ella', 'Aïcha', 'Dounia', 'Béa', 'Ella', 'Dounia', 'Ella', 'Béa', 'Béa',
             'Cléa', 'Cléa', 'Béa', 'Dounia', 'Dounia', 'Cléa', 'Béa', 'Cléa', 'Béa', 'Aïcha',
             'Aïcha', 'Béa', 'Aïcha', 'Cléa', 'Ella', 'Béa', 'Ella', 'Béa', 'Ella', 'Ella', 'Cléa',
             'Aïcha', 'Béa', 'Ella']
assert conv_dict(liste_vic, amies) == {'Aïcha': 25, 'Béa': 34, 'Cléa': 27, 'Dounia':
                                       30, 'Ella': 34}


# 4

def nom_indien(first_name: str, last_name: str):
    PREMIERE_PARTIE = {'A': 'Aigle',
                       'B': 'Buse',
                       'C': 'Chacal',
                       'D': 'Doryphore',
                       'E': 'Ecureuil',
                       'F': 'Fleuve',
                       'G': 'Grenouille',
                       'H': 'Horizon',
                       'I': 'Iris',
                       'J': 'Jaguar',
                       'K': 'Kangourou',
                       'L': 'Loutre',
                       'M': 'Mésange',
                       'N': 'Neige',
                       'O': 'Ours',
                       'P': 'Pluie',
                       'Q': 'Quetzal',
                       'R': 'Renard',
                       'S': 'Sauterelle',
                       'T': 'Tourterelle',
                       'U': 'Ululement',
                       'V': 'Vent',
                       'W': 'Weigélia',
                       'X': 'Xérus',
                       'Y': 'Yak',
                       'Z': 'Zibeline'}
    SECONDE_PARTIE = {'A': ' agile',
                      'B': ' de braise',
                      'C': ' qui chante',
                      'D': ' qui danse',
                      'E': ' qui écoute',
                      'F': ' de feu',
                      'G': ' des glaces',
                      'H': ' humide',
                      'I': ' invincible',
                      'J': ' juvénile',
                      'K': ' kamikaze',
                      'L': ' de lumière',
                      'M': ' du matin',
                      'N': ' nocturne',
                      'O': ' de l\'ombre',
                      'P': ' paisible',
                      'Q': ' sans querelle',
                      'R': ' qui rit',

                      'S': ' du soir',
                      'T': ' taciturne',
                      'U': ' ultime',
                      'V': ' qui voit',
                      'W': ' en week-end',
                      'X': ' xylophoniste',
                      'Y': ' yoyotant',
                      'Z': ' zig-zaguant'}

    return f"{PREMIERE_PARTIE[first_name[0].upper()]}{SECONDE_PARTIE[last_name[0].upper()]}"


assert nom_indien('John', 'Doe') == 'Jaguar qui danse'
assert nom_indien('Elsa', 'Kumaï') == 'Ecureuil kamikaze'
assert nom_indien('Tara', 'Waliz') == 'Tourterelle en week-end'


# 5

def frequence_lettre(string: str):
    chars = string.split("")
    dic = {}
    for char in chars:
        dic[char] = 1
