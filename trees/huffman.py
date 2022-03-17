from arbre_binaire_3 import ABR


def dico_frequences(txt: str):
    """
    >>> texte = "anticonstitutionnellement"
    >>> dico_frequences(texte)
    {'a': 1, 'n': 5, 't': 5, 'i': 3, 'c': 1, 'o': 2, 's': 1, 'u': 1, 'e': 3, 'l': 2, 'm': 1}
    """
    dic = {}

    for c in txt:
        if not dic.get(c):
            dic[c] = 0

        dic[c] += 1

    return dic


def creer_tab_feuille(txt: str):
    """
    >>> creer_tab_feuille("aabbbc")
    [{'r': ('c', 1), 'g': {'r': None, 'g': None, 'd': None}, 'd': {'r': None, 'g': None, 'd': None}}, {'r': ('a', 2), 'g': {'r': None, 'g': None, 'd': None}, 'd': {'r': None, 'g': None, 'd': None}}, {'r': ('b', 3), 'g': {'r': None, 'g': None, 'd': None}, 'd': {'r': None, 'g': None, 'd': None}}]
    """
    freq = [*dico_frequences(txt).items()]
    trees = []
    for f in freq:
        trees.insert(f[1]-1, ABR(f, ABR(), ABR()))

    return trees


def creer_arbre(t):
    print(t)

    if len(t) == 1:
        return t

    twos = t[:2]

    _sum = 0
    for i in twos:
        _sum += i.racine()[1]

    a = ABR(_sum, *twos)
    t.pop(0)
    t.pop(1)

    t.insert(_sum, a)

    return creer_arbre(t)


creer_arbre(creer_tab_feuille("aabbbc"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
