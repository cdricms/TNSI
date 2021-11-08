
def recherche(tab: list, n: int):
    last_occ = len(tab)

    for x in range(len(tab)):
        if tab[x] == n:
            last_occ = x

    return last_occ


print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))
