class ArbreBinaire:
    """
    Classe Arbre Binaire
    """

    def __init__(self, racine=None, gauche=None, droit=None):
        self.r = racine
        self.g = gauche
        self.d = droit

    def est_vide(self):
        return self.r == None

    def racine(self):
        if not self.est_vide():
            return self.r

    def gauche(self):
        if not self.est_vide():
            return self.g

    def droite(self):
        if not self.est_vide():
            return self.d

    def __str__(self):
        return str(self.__dict__)

    __repr__ = __str__

    def parcours_prefixe(self):

        if not self.est_vide():
            print(self.r)
            self.g.parcours_prefixe()
            self.d.parcours_prefixe()

    def parcours_infixe(self):

        if not self.est_vide():
            self.g.parcours_infixe()
            print(self.r)
            self.d.parcours_infixe()

    def parcours_postfixe(self):

        if not self.est_vide():
            self.g.parcours_postfixe()
            self.d.parcours_postfixe()
            print(self.r)

    def parcours_largeur(self):
        pass


        # arbre vide
vide = ArbreBinaire()
# création de l'arbre du 'A vous de jouer ! (5)'
k = ArbreBinaire('k', vide, vide)
f = ArbreBinaire('f', vide, vide)
e = ArbreBinaire('e', k, vide)
b = ArbreBinaire('b', e, f)
m = ArbreBinaire('m', vide, vide)
j = ArbreBinaire('j', m, vide)
i = ArbreBinaire('i', vide, vide)
d = ArbreBinaire('d', i, j)
h = ArbreBinaire('h', vide, vide)
c = ArbreBinaire('c', vide, h)
a = ArbreBinaire('a', c, d)
arbre = ArbreBinaire('r', a, b)

# print(arbre)

print(arbre.gauche())


arbre.parcours_largeur()
