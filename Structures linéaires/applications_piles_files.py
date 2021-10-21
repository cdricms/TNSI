from piles_files import empty_stack, stack_push, is_stack_empty, stack_pop, stack_top


# Application 1
def copie_pile(pile: list):
    return [*pile]


# Application 2
def separe_pile(pile: list):
    even = empty_stack()
    odd = empty_stack()

    for item in pile:
        if item % 2 == 0:
            stack_push(even, item)
        else:
            stack_push(odd, item)

    return even, odd


pile = empty_stack()
stack_push(pile, 2)
stack_push(pile, 5)
stack_push(pile, 4)
print(separe_pile(pile))


# Application 3
def est_bien_parenthesee(string: str):
    p = empty_stack()
    answer = False

    opened = ["(", "{", "<", "["]
    closed = [")", "}", ">", "]"]

    for char in string:
        if char in opened:
            stack_push(p, char)
        elif char in closed:
            if is_stack_empty(p):
                answer = False
            else:
                _p = stack_pop(p)
                if _p in opened:
                    answer = True

    return answer


print(est_bien_parenthesee('(((((())))))'))
print(est_bien_parenthesee('(((((<>())))))'))
print(est_bien_parenthesee('((((())))))'))
print(est_bien_parenthesee('((((<>())))))'))


# Application 4

def polo(string: str):
    chars = string.split()
    pile = empty_stack()
    operators = ['+', '-', '/', '*']

    for char in chars:
        if char.isdecimal():
            stack_push(pile, int(char))
        elif char in operators:
            a = stack_pop(pile)
            b = stack_pop(pile)
            if char == "+":
                stack_push(pile, a+b)
            elif char == "-":
                stack_push(pile, a-b)
            elif char == "/":
                stack_push(pile, a/b)
            elif char == "*":
                stack_push(pile, a*b)

    return stack_top(pile)


print(polo('3 4 +'))
print(polo('2 3 + 5 4 + *'))
