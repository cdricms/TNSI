from typing import Tuple


def division_euclidienne(numerateur: int, denominateur: int) -> tuple:


    """
    Fonction effectuant la division euclidienne de a par b en utilisant
    l'algorithme par soustraction. Renvoie un doublet (quotient,reste), de
    sorte que a = quotient*b + reste avec 0 <= reste < b.
    entrées: a et b (int) nombre et diviseur
    sorties: (int,int) quotient, reste
    Preconditions: a >= 0 et b > 0 avec a et b entiers.
    Si les préconditions ne sont pas respectées, doit renvoyer -1.
    Cas "normaux" de division euclidienne
    >>> division_euclidienne(10, 2)
    (5, 0)
    >>> division_euclidienne(2, 10)
    (0, 2)
    >>> division_euclidienne(37, 3)
    (12, 1)
    >>> division_euclidienne(-10, 7)
    -1
    >>> division_euclidienne(10, -7)
    -1
    >>> division_euclidienne(10.3, 4)
    -1
    >>> division_euclidienne(11, 3.5)
    -1

    >>> division_euclidienne(0, 3)
    (0, 0)
    >>> division_euclidienne(3, 0)
    -1
    >>> division_euclidienne(0, 0)
    -1
    """

    if numerateur < 0 or denominateur < 0:
        return -1
    
    if isinstance(numerateur, float) or isinstance(denominateur, float):
        return -1

    quotient = 0
    dem_copy = denominateur
    remaining = numerateur
    while remaining >= dem_copy:
        remaining -= dem_copy
        quotient += 1
    return quotient, remaining


def test_division_euclidienne():
    '''
    Teste certaines propriétés de la fonction division_euclidienne
    Lève une exception AssertionError si la fonction est mal programmée

    entrée: -
    sortie:-
    '''
    assert division_euclidienne(10, 2) == (5, 0)
    assert division_euclidienne(2, 10) == (0, 2)
    assert division_euclidienne(37, 3) == (12, 1)
    assert division_euclidienne(-10, 7) == -1
    assert division_euclidienne(10, -7) == -1
    assert division_euclidienne(10.3, 4) == -1
    assert division_euclidienne(11, 3.5) == -1
    assert division_euclidienne(3, 0) == -1
    assert division_euclidienne(0, 3) == (0, 0)
    assert division_euclidienne(0, 0) == -1


# on lance les tests
# test_division_euclidienne()

### Durant le développement, le programme ne se termine jamais, à décommenter pour essayer.

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # assert division_euclidienne(26, 3) == (8, 2)
    # assert division_euclidienne(12, 6) == (2, 0)
    
    
    
