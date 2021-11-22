def maxi(tab: list):
    """
    >>> maxi([1,5,6,9,1,2,3,7,9,8])
    (9, 3)
    """
    index = 0
    highest = 0

    for i in range(len(tab)):
        if tab[i] > highest:
            highest = tab[i]
            index = i

    return (highest, index)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
