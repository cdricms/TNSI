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
victories = []


def conv_dict(victories: list)


dic = {}
for name in victories:
     if name.keys()
      count = 0
       for victory in victories:
            if name == victory:
                count += 1
        dic[f"{name}"] = count
