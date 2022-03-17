def is_in_sequence_recursive(seq: list, n: int, beg: int, end: int):
    """
    >>> a = [1, 2, 3, 4, 5, 6, 258]
    >>> is_in_sequence_recursive(a, 5, 0, len(a)-1)
    True
    >>> is_in_sequence_recursive(a, 170, 0, len(a)-1)
    False
    """
    middle = int((beg+end)/2)
    if seq[middle] == n:
        return True
    if end-beg < 2:
        return False

    if seq[middle] < n:
        return is_in_sequence_recursive(seq, n, middle, end)
    else:
        return is_in_sequence_recursive(seq, n, beg, middle)


def get_index_recursive(seq: list, n: int, beg: int, end: int):
    """
    >>> a = [1, 2, 3, 4, 5, 6, 258]
    >>> get_index_recursive(a, 5, 0, len(a)-1)
    4
    >>> get_index_recursive(a, 170, 0, len(a)-1)
    -1
    """
    middle = int((beg+end)/2)
    if seq[middle] == n:
        return middle
    if end-beg < 2:
        return -1

    if seq[middle] < n:
        return get_index_recursive(seq, n, middle, end)
    else:
        return get_index_recursive(seq, n, beg, middle)


def get_index_hello_recursive(seq: list, beg, end):
    """
    >>> a = ["bonjour", "hello", "salut", "test", "ok", "coucou"]
    >>> get_index_hello_recursive(a, 0, len(a)-1)
    1
    >>> b = ["bonjour", "salut", "test", "ok", "coucou"]
    >>> get_index_hello_recursive(b, 0, len(b)-1)
    -1
    """
    middle = int((beg+end)/2)

    if seq[middle] == "hello":
        return middle
    if end-beg < 2:
        return -1

    if seq[middle] < "hello":
        return get_index_hello_recursive(seq, middle, end)
    else:
        return get_index_hello_recursive(seq, beg, middle)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
