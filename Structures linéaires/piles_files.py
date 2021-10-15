def empty_stack(): return []


def is_stack_empty(stack: list):
    """
    - prend en paramètre une pile pile
    - renvoie True si la pile est vide et False sinon
    Exemple :
    >>> is_stack_empty([])
    True
    >>> is_stack_empty([1])
    False
    """
    return stack_len(stack) == 0


def stack_top(stack: list):
    """
    - prend en paramètre une pile pile
    - renvoie le sommet de la pile
    Exemples :
    >>> stack_top([2, 3, 5])
    5
    >>> print(stack_top([]))
    None
    """
    if stack_len(stack) > 0:
        return stack[-1]

    return None


def stack_push(stack: list, el):
    """
    - prend en paramètre une pile et un élément el
    - empile l’élément el
    Exemples :
    >>> pile = [2, 3]
    >>> pile = stack_push(pile, 5)
    >>> pile
    [2, 3, 5]
    """
    stack += [el]
    return stack


def stack_pop(stack: list):
    """
    - prend en paramètre une pile pile
    - dépile le dernier élément saisi
    - renvoie le sommet de la pile
    Exemples :
    >>> stack_pop([2, 3, 5])
    5
    >>> print(stack_pop([]))
    None
    """
    if stack_len(stack) > 0:
        return stack.pop()

    return None


def stack_len(stack: list):
    count = 0
    for el in stack:
        count += 1

    return count


def main():
    stack = empty_stack()
    print(stack)
    stack_push(stack, 5)
    stack_push(stack, 50)
    print(stack)

    stack_pop(stack)
    print(stack)

    print(is_stack_empty(stack))

    print(stack_len(stack))


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
