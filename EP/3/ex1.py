def recherche(elt: int, tab: list):
    """
    >>> recherche(3, [3, 2, 1, 3, 2, 1])
    [0, 3]
    >>> recherche(4, [1, 2, 3])
    []
    """
    return [x for x in range(len(tab)) if tab[x] == elt]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
