def recherche(el, tab):
    """
    >>> recherche(1,[2,3,4])
    -1
    >>> recherche(1,[10,12,1,56])
    2
    >>> recherche(1,[1,50,1])
    2
    >>> recherche(1,[8,1,10,1,7,1,8])
    5
    """
    last_occ = -1
    for x in range(len(tab)):
        if tab[x] == el:
            last_occ = x

    return last_occ


if __name__ == "__main__":
    import doctest
    doctest.testmod()
