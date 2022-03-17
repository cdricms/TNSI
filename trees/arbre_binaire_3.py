class ABR:
    """
    Classe Arbre Binaire de Recherche
    """

    def __init__(self, racine=None, gauche=None, droit=None):
        self.r = racine
        self.g = gauche
        self.d = droit

    def __repr__(self):
        return str(self.__dict__)

    def racine(self):
        return self.r

    def gauche(self):
        return self.g

    def droite(self):
        return self.d

    def est_vide(self):
        return self.r is None

    def est_feuille(self):
        return self.gauche().est_vide() and self.droite().est_vide()

    def hauteur(self):
        if self.est_vide():
            return -1
        return 1 + max(self.gauche().hauteur(), self.droite().hauteur())

    def taille(self):
        if self.est_vide():
            return 0
        return 1 + self.gauche().taille() + self.droite().taille()

    def parcours_prefixe(self):
        if not self.est_vide():
            print(self.racine(), end=' ')
            self.gauche().parcours_prefixe()
            self.droite().parcours_prefixe()

    def parcours_infixe(self):
        if not self.est_vide():
            self.gauche().parcours_infixe()
            print(self.racine(), end=' ')
            self.droite().parcours_infixe()

    def parcours_infixe_l(self):
        result = []
        if not self.est_vide():
            result += self.gauche().parcours_infixe_l()
            result.append(self.racine())
            result += self.droite().parcours_infixe_l()

        return result

    def parcours_postfixe(self):
        if not self.est_vide():
            self.gauche().parcours_postfixe()
            self.droite().parcours_postfixe()
            print(self.racine(), end=' ')

    def parcours_largeur(self):
        f = File()
        f.enfile(self)
        while not f.est_vide():
            x = f.defile()
            print(x.racine(), end=' ')
            if not x.gauche().est_vide():
                f.enfile(x.gauche())
            if not x.droite().est_vide():
                f.enfile(x.droite())

    def creer_feuille(self, val):
        self.r = val
        self.g = ABR()
        self.d = ABR()

    def is_in_tree(self, val):
        if self.est_vide():
            return False

        if val < self.racine():
            return self.gauche().is_in_tree(val)
        elif val > self.racine():
            return self.droite().is_in_tree(val)

        return True

    def inserer(self, val):
        if self.est_vide():
            return self.creer_feuille(val)

        if val < self.racine():
            return self.gauche().inserer(val)
        elif val > self.racine():
            return self.droite().inserer(val)

    def insert_d(self, val):
        if self.est_vide():
            return self.creer_feuille(val)

        if val <= self.racine():
            return self.gauche().inserer(val)
        elif val > self.racine():
            return self.droite().inserer(val)

    def sort(l: list) -> list:
        tree = ABR()
        for i in l:
            tree.insert_d(i)

        result = tree.parcours_infixe_l()

        return result

    def max(self):
        a = self
        root = a.racine()
        while not a.est_vide():
            root = a.racine()
            a = a.droite()

        return root

    def min(self):
        a = self
        root = a.racine()
        while not a.est_vide():
            root = a.racine()
            a = a.gauche()

        return root

    def get_value(self, v: str):
        l = self.parcours_infixe_l()


class File:
    """
    Classe pour File
    """

    def __init__(self):
        self.f = []

    def est_vide(self):
        return self.f == []

    def enfile(self, el):
        self.f.append(el)

    def defile(self):
        if not self.est_vide():
            return self.f.pop(0)


# arbre vide -> ABR()
# création de l'arbre du II.
arbre = ABR(6, ABR(3, ABR(1, ABR(), ABR(2, ABR(), ABR())), ABR(4, ABR(), ABR(5, ABR(), ABR()))),
            ABR(8, ABR(7, ABR(), ABR()), ABR(9, ABR(), ABR())))


def is_in_tree(tree, val):
    if tree.est_vide():
        return False

    if val < tree.racine():
        return is_in_tree(tree.gauche(), val)
    elif val > tree.racine():
        return is_in_tree(tree.droite(), val)

    return True


def insert(tree, val):
    if tree.est_vide():
        return tree.creer_feuille(val)

    if val < tree.racine():
        return insert(tree.gauche(), val)
    elif val > tree.racine():
        return insert(tree.droite(), val)


def creer_arbre(l: list):
    arbre = ABR()
    for i in l:
        arbre.inserer(i)

    return arbre


def creer_arbre_d(l: list):
    arbre = ABR()
    for i in l:
        arbre.insert_d(i)

    return arbre


# print(is_in_tree(arbre, 9))
# print(arbre.is_in_tree(9))
# arbre.inserer(12)
# print(arbre)
# insert(arbre, 13)
# print(arbre)

# a = creer_arbre([2, 5, 4, 6, 7])
# print(a)

# a1 = creer_arbre([3, -2, 5, -6, 7, 1, 8, -4, 2, 10, -7])
# print(a1)
# a2 = creer_arbre(["chien", "poule", "mouton", "brebis",
    # "cheval", "chat", "ours", "renard"])
# print(a2)

# A3 = creer_arbre_d([3,-2,5,-6,7,1,8,-4,2,10,-7,5,3,-6,8,-4,10,-2,1])
# print(A3)
# A4 = creer_arbre_d(["chien","poule","mouton","brebis","cheval","chat",
# "ours","renard","mouton","poule","chat","cheval","chien"])
# print(A4)
if __name__ == "__main__":

    print(ABR.sort([-5, -8, 5, 7, 9, -256]))
    a = creer_arbre([-5, -8, 5, 7, 9, -256])

    print(a.max())
    print(a.min())

    b = creer_arbre(["chat", "chien", "souris", "araignée",
                    "crapaud", "grenouille", "lézard", "zèbre"])

    b.get_value("chat")
