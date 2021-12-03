
def recherche(caractere: str, mot: str):
    """
    >>> recherche('e', "sciences")
    2
    >>> recherche('i',"mississippi")
    4
    >>> recherche('a',"mississippi")
    0
    """

    counter = 0
    for c in mot:
        if c == caractere:
            counter += 1

    return counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
