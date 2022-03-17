def noeud(nom, fg=None, fd=None):
    return {'racine': nom, 'fg': fg, 'fd': fd}


def construit(arbre):
    if arbre == None:
        return []
    else:
        return [arbre['racine'], construit(arbre['fg']), construit(arbre['fd'])]


# création des noeuds du 'A vous de jouer ! (5)'
k = noeud('k')
f = noeud('f')
e = noeud('e', k, None)
b = noeud('b', e, f)
m = noeud('m')
j = noeud('j', m, None)
i = noeud('i')
d = noeud('d', i, j)
h = noeud('h')
c = noeud('c', None, h)
a = noeud('a', c, d)
racine = noeud('r', a, b)
# création de l'arbre du 'A vous de jouer ! (5)'
arbre = construit(racine)
print(arbre)


def est_vide(arbre):
    return arbre == []


def racine(arbre):
    if arbre and not est_vide(arbre):
        return arbre[0]


def gauche(arbre):
    if arbre and not est_vide(arbre):
        return arbre[1]


def droit(arbre):
    if arbre and not est_vide(arbre):
        return arbre[2]


def parcours_prefixe(arbre):
    if not est_vide(arbre):
        print(racine(arbre))
        parcours_prefixe(gauche(arbre))
        parcours_prefixe(droit(arbre))


print("__________________")
parcours_prefixe(arbre)


def parcours_infixe(arbre):
    if not est_vide(arbre):
        parcours_postfixe(gauche(arbre))
        print(racine(arbre))
        parcours_postfixe(droit(arbre))


def parcours_postfixe(arbre):
    if not est_vide(arbre):
        parcours_postfixe(gauche(arbre))
        parcours_postfixe(droit(arbre))
        print(racine(arbre))


print("__________________")
parcours_postfixe(arbre)


def parcours_largeur(arbre):
    f = []
    x = None

    f += arbre
    print(f)

    while not est_vide(f):
        x = f.pop(0)
        print(racine(x))
        if not est_vide(a := gauche(x)):
            f += a
        if not est_vide(b := droit(x)):
            f += b


print("__________________")
parcours_largeur(arbre)
