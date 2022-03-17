

def taille(arbre: dict, lettre):
    """
    >>> a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
    'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
    'H':['','']}
    >>> taille(a, "F")
    9
    """

    node = arbre[lettre]

    i = 1
    for n in node:
        if n != '':
            i += taille(arbre, n)

    return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
