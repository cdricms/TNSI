def tri_selection(l: list):
    """
    >>> tri_selection([1,52,6,-9,12])
    [-9, 1, 6, 12, 52]
    """
    for i in range(len(l)):
        lowest = i
        for j in range(i, len(l)):
            if l[j] < l[lowest]:
                lowest = j
        l[i], l[lowest] = l[lowest], l[i]
    return l


if __name__ == "__main__":
    import doctest
    doctest.testmod()
