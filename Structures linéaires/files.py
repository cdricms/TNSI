def f_vide():
    """
    - sans paramètre
    - renvoie une file vide
    Exemple :
    >>> f_vide()
    []
    """
    # A COMPLETER

    return []


def f_est_vide(file):
    """
    - prend en paramètre une file file
    - renvoie True si la file est vide et False sinon
    Exemple :
    >>> f_est_vide([])
    True
    >>> f_est_vide([1])
    False
    """
    # A COMPLETER

    return len(file) == 0


def f_tete(file):
    """
    - prend en paramètre une file
    - renvoie la tête de la file ou None si la file est vide
    Exemple :
    >>> f_tete([2, 3, 5])
    2
    >>> print(f_tete([]))
    None
    """
    # A COMPLETER

    if len(file) > 0:
        return file[0]

    return None


def f_enfile(file, el):
    """
    - prend en paramètre une file et un élément el
    - enfile une élément el à l'arrière de la file
    Exemple :
    >>> file = [2, 3, 5, 8]
    >>> f_enfile(file, 1)
    >>> file
    [2, 3, 5, 8, 1]
    """
    # A COMPLETER

    return file.append(el)


def f_defile(file):
    """
    - prend en paramètre une file
    - défile l'élément situé à l'avant de la file
    - renvoie l’élément défilé ou None si la file est vide
    Exemple :
    >>> file = [2, 3, 5, 8]
    >>> f_defile(file)
    2
    >>> file
    [3, 5, 8]
    """
    # A COMPLETER

    if len(file) > 0:
        return file.pop(0)

    return None


def f_longueur(file):
    count = 0
    for el in file:
        count += 1

    return count


if __name__ == "__main__":
    from doctest import testmod

    testmod()
