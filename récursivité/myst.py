def myst(l: list):
    if l == []:
        return 0
    else:
        l.pop(0)
        return 1 + myst(l)


print(myst([1, 5, 6, 4, 5, 8]))
print(myst(["c", "é", "d", "r", "i", "c"]))

# C'est la fonction len
