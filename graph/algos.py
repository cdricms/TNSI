g = dict()
g['a'] = ['b', 'c']
g['b'] = ['a', 'd', 'e']
g['c'] = ['a', 'd']
g['d'] = ['b', 'c', 'e']
g['e'] = ['b', 'd', 'f', 'g']
g['f'] = ['e', 'g']
g['g'] = ['e', 'f', 'h']
g['h'] = ['g']


def dfs(G, s):
    visited = []
    p = [s]

    while len(p) > 0:
        x = p.pop()
        if x not in visited:
            visited.append(x)

        for v in G[x]:
            if v not in visited:
                p.append(v)

    return visited


print(dfs(g, 'b'))


def dfs_r(G, s):
    visited = []

    def d(G, s):
        visited.append(s)
        for v in G[s]:
            if v not in visited:
                d(G, v)

        return visited

    d(G, s)
    return visited


print(dfs_r(g, 'b'))


def bfs(G, s):
    visited = []
    f = [s]
    while len(f) > 0:
        x = f.pop(0)
        if x not in visited:
            visited.append(x)

        for v in G[x]:
            if v not in visited:
                f.append(v)

    return visited


print(bfs(g, 'b'))


def has_cycle(G, s):
    visited = []
    p = [s]
    while len(p) > 0:
        x = p.pop()
        if x not in visited:
            visited.append(x)

        for v in G[s]:
            if v not in visited:
                p.append(v)
            else:
                return True

    return False


print(has_cycle(g, 'b'))


def bfs_p(G, s):
    visited = []
    parents = {}
    parents[s] = None

    f = [s]

    while len(f) > 0:
        x = f.pop(0)
        if x not in visited:
            visited.append(x)

        for v in G[s]:
            if v not in visited:
                f.append(v)
                parents[v] = x

    return parents


print(bfs_p(g, 'b'))
