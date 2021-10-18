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
    dic = {}
    for char in string:
        if char not in dic.keys():
            dic[char] = 1
        else:
            dic[char] += 1

    return dic


assert(frequence_lettre('toto')) == {'t': 2, 'o': 2}
assert(frequence_lettre('bonjour')) == {
    'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}
assert(frequence_lettre('anticonstitutionnellement')) == {'a': 1, 'n': 5, 't': 5, 'i':
                                                          3, 'c': 1, 'o': 2, 's': 1, 'u': 1, 'e': 3, 'l': 2, 'm': 1}


# 6

puiss_2 = {n: 2**n for n in range(21)}
print(puiss_2)


# 7
soldes = {'12P45': 1288.59, '34F89': 584.46, '86L21': 8451.36, '87T56': 41.25,
          '21P21': -12.84, '89Y67': 2354.41, '88L91': 15647.98, '44V65': 687.10, '96Q78':
          3457.91, '77X04': 864.29}
soldes_sup = {key: value for key, value in soldes.items() if value > 1000}
print(soldes_sup)


# 8
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
           "15", "16", "17", "18", "19", "2A", "2B", "21", "22", "23", "24", "25", "26", "27", "28",
           "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43",
           "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58",
           "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73",
           "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
           "89", "90", "91", "92", "93", "94", "95", "971", "972", "973", "974", "976"]

noms = ["Ain", "Aisne", "Allier", "Alpes-de-Haute-Provence", "Hautes-Alpes", "Alpes-Maritimes", "Ardèche", "Ardennes", "Ariège", "Aube", "Aude", "Aveyron", "Bouches-du-Rhône", "Calvados", "Cantal", "Charente", "Charente-Maritime", "Cher", "Corrèze", "Corse-du-Sud", "Haute-Corse", "Côte-d'Or", "Côtes d'Armor", "Creuse", "Dordogne", "Doubs", "Drôme", "Eure", "Eure-et-Loir", "Finistère", "Gard", "Haute-Garonne", "Gers", "Gironde", "Hérault", "Ille-et-Vilaine", "Indre", "Indre-et-Loire", "Isère", "Jura", "Landes", "Loir-et-Cher", "Loire", "Haute-Loire", "Loire-Atlantique", "Loiret", "Lot", "Lot-et-Garonne", "Lozère", "Maine-et-Loire", "Manche", "Marne",
        "Haute-Marne", "Mayenne", "Meurthe-et-Moselle", "Meuse", "Morbihan", "Moselle", "Nièvre", "Nord", "Oise", "Orne", "Pas-de-Calais", "Puy-de-Dôme", "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Pyrénées-Orientales", "Bas-Rhin", "Haut-Rhin", "Rhône", "Haute-Saône", "Saône-et-Loire", "Sarthe", "Savoie", "Haute-Savoie", "Paris", "Seine-Maritime", "Seine-et-Marne", "Yvelines", "Deux-Sèvres", "Somme", "Tarn", "Tarn-et-Garonne", "Var", "Vaucluse", "Vendée", "Vienne", "Haute-Vienne", "Vosges", "Yonne", "Territoire de Belfort", "Essonne", "Hauts-de-Seine", "Seine-St-Denis", "Val-de-Marne", "Val-D'Oise", "Guadeloupe", "Martinique", "Guyane", "La Réunion", "Mayotte"]

departements = {numeros[x]: noms[x] for x in range(len(numeros))}
print(departements)


# 9
ages = {'Mirza': 7, 'Tom': 4, 'Moustache': 6, 'Patoune': 5, 'Frisco': 6, 'Tacos':
        5, 'Sleepy': 3, 'Belle': 4, 'Zaza': 11, 'Oxmo': 13}

chats_ages = [name for name, age in ages.items() if age > 7]
print(chats_ages)
