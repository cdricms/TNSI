def moyenne(tab: list):
    """
    >>> moyenne([5, 3, 8])
    5.333333333333333
    >>> moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    5.5
    >>> moyenne([])
    'erreur'
    """

    if tab == []:
        return "erreur"

    average = 0
    for x in tab:
        average += x

    return average / len(tab)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
