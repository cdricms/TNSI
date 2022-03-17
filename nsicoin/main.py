

def verification(x: int, y: int, p: int) -> bool:
    """
    >>> p = 15486869
    >>> verification(6543210, 8371779, p)
    True
    """
    return x**2 % p == y


def racine(y: int, p: int):
    """
    >>> p = 15486869
    >>> racine(8371779, p)
    6543210
    """
    import math
    for x in range(y):
        if verification(x, y, p):
            return x


def racine_approche(y: int, p: int, marge: int):
    """
    >>> p = 15486869
    >>> racine_approche(8371779, p, 20)
    413988
    """
    for x in range(y):
        if (x**2-y) % p <= marge:
            return x


def addition(l1: list, l2: list):
    """
    >>> addition([1,2,3,4,5,6],[1,1,1,98,98,98])
    [2, 3, 4, 2, 3, 4]
    """
    assert len(l1) == len(l2)

    result = []
    for i in range(len(l1)):
        result.append((l1[i] + l2[i]) % 100)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
