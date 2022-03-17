def creation_arbre(r, hauteur):
    """
    Entrée(s) : r (racine) de type str ou int, hauteur (de l’arbre) de type (int)
    Sortie de type list
    """
    return [r] + [None for i in range(2**(hauteur+2)-2)]


def insertion_noeud(arbre, noeud, fg, fd):
    """
    Insére les noeuds et leurs enfants dans l’arbre
    """
    indice = arbre.index(noeud)
    arbre[2 * indice+1] = fg
    arbre[2 * indice+2] = fd


# création de l’arbre du 'A vous de jouer ! (5)'
arbre = creation_arbre("r", 4)
# ajout des noeuds par niveau de gauche à droite
insertion_noeud(arbre, "r", "a", "b")
insertion_noeud(arbre, "a", "c", "d")
insertion_noeud(arbre, "b", "e", "f")
insertion_noeud(arbre, "c", None, "h")
insertion_noeud(arbre, "d", "i", "j")
insertion_noeud(arbre, "e", "k", None)
insertion_noeud(arbre, "f", None, None)
insertion_noeud(arbre, "h", None, None)
insertion_noeud(arbre, "i", None, None)
insertion_noeud(arbre, "j", "m", None)
insertion_noeud(arbre, "k", None, None)
insertion_noeud(arbre, "m", None, None)
# pour vérifier
print(len(arbre))
print(arbre)


def parent(arbre, noeud):
    if noeud in arbre:
        indice = arbre.index(noeud)

    if indice % 2 == 0:
        return arbre[(indice-2)//2]
    else:
        return arbre[(indice-1)//2]


def est_vide(arbre):
    return len(arbre) == 0


def fils_gauche(arbre, noeud):
    idx = arbre.index(noeud)
    return arbre[2*idx+1]


def fils_droite(arbre, noeud):
    idx = arbre.index(noeud)
    return arbre[2*idx+2]


def est_racine(arbre, noeud):
    return arbre.index(noeud) == 0


def est_feuille(arbre, noeud):
    fd = fils_droite(arbre, noeud)
    fg = fils_gauche(arbre, noeud)

    return fd == None and fg == None


def est_frere(arbre, noeud):
    _parent = parent(arbre, noeud)
    fd = fils_droite(arbre, _parent)
    fg = fils_gauche(arbre, _parent)

    if fd == noeud and fg:
        return True
    elif fg == noeud and fd:
        return True

    return False


arbre = creation_arbre("r", 2)

insertion_noeud(arbre, "r", "a", "b")
insertion_noeud(arbre, "a", "c", "d")
insertion_noeud(arbre, "b", "e", "f")

print(arbre)


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
    return len(arbre) == 0


def racine(arbre):
    if not est_vide(arbre):
        return arbre[0]


def gauche(arbre):
    if len(arbre) == 2:
        return arbre[1]


def droit(arbre):
    if len(arbre) == 3:
        return arbre[2]
