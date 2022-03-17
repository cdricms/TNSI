
def nbr_s(G): return len(G)


def nbr_a(G):
    c = 0
    for i in G.values():
        c += len(i)

    return c


def deg_s(G, s):
    v = G.get(s)
    assert v

    return len(v)


def n(G, s):
    v = G.get(s) or []

    return v


def highest_s(G):
    highest = 0
    k = None
    for (key, value) in G.items():
        if len(value) > highest:
            highest = len(value)
            k = key

    return k


G = {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'd'], 'd': ['b', 'c', 'e'], 'e': ['b',
                                                                                         'd', 'f', 'g'], 'f': ['e', 'g'], 'g': ['e', 'f', 'h'], 'h': ['g']}


G = {"a": ["b", "d", "c"], "b": ["a", "d"], "c": ["a", "d", "e"], "d": [
    "a", "b", "c", "e", "f"], "e": ["c", "d", "f"], "f": ["d", "e"]}

# print(nbr_s(G))
# print(nbr_a(G))
# print(deg_s(G,  "b"))
# print(n(G, "a"))
print(highest_s(G))
