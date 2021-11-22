def positif(T):
    """
    >>> positif([-1,0,5,-3,4,-6,10,9,-8 ])
    T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
    [0, 5, 4, 10, 9]
    """
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T =', T)
    return T2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
