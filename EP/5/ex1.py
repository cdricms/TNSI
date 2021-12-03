def multiplication(n1: int, n2: int):
    """
    >>> multiplication(3,5)
    15
    >>> multiplication(-4,-8)
    32
    >>> multiplication(-2,6)
    -12
    >>> multiplication(-2,0)
    0
    """
    result = 0
    r = n1 if n1 > 0 else 0-n1
    for x in range(r):
        if n1 < 0 or n2 < 0:
            result -= n2
        else:
            result += n2

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
