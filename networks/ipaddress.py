address = "115.250.207.0"


def addstr_to_int(ip: str):
    """
    Entrée(s) : ip_str de type str
    Sortie : type int
    >>> addstr_to_int("115.250.207.0")
    1945816832
    """
    a = ip.split(".")
    return int(a[0]) * 2**24 + int(a[1]) * 2 ** 16 + int(a[2]) * 2 ** 8 + int(a[3])


def addint_to_str(ip: int):
    """
    >>> addint_to_str(1945816832)
    '115.250.207.0'
    """
    x = 24
    result = [str(int(ip / 2 ** x))]
    r = ip % 2 ** x
    x = 16
    for i in range(3):
        result.append(str(int(r / 2 ** x)))
        r %= 2 ** x
        x -= 8

    return ".".join(result)


def adresse_reseau_ip(ip, masque):
    """
    Entrée(s) : ip, masque de type str
    Sortie : type str
    >>> adresse_reseau_ip( "115.250.207.0","255.255.240.0")
    '115.250.192.0'
    """

    mask = addstr_to_int(masque)

    i = addstr_to_int(ip)

    return addint_to_str(mask & i)


def nbr_machines(masque):
    """
    Entrée(s) : masque de type str
    Sortie : type int
    >>> nbr_machines('255.255.240.0')
    4094
    """
    l = str(bin(addstr_to_int(masque)))[2:].count("0")

    return (2 ** l) - 2


def adresse_reseau_cidr(ipcidr):
    """
    Entrée(s) : ipcidr de type str
    Sortie : type str
    >>> adresse_reseau_cidr("115.250.207.0/20")
    '115.250.192.0'
    """

zsh:1: command not found: q
    i = addstr_to_int(ip)
    bin_c = b'c * "1" + 32-c * "0"'
    print(bin(bin_c))

    return addint_to_str(mask & i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
