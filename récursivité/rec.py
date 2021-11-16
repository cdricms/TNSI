def somme_iter(n):
    count = 0
    for i in range(n+1):
        count += i

    return count


print(somme_iter(10))
print(somme_iter(15))


def somme_rec(n):
    if n == 0:
        return 0

    return n + somme_rec(n-1)


print(somme_rec(10))
print(somme_rec(15))

# print(somme_iter(100))
# print(somme_iter(1_000_000))
# print(somme_rec(100))
# print(somme_rec(1_000_000))


def somme_rec_2(n):
    assert(n > 0)
    return somme_rec(n)


print(somme_rec_2(10))


def fibo_rec(n):
    if n == 0 or n == 1:
        return 1
    return fibo_rec(n-2)+fibo_rec(n-1)


print(fibo_rec(5))


def fibo_iter(n):
    last = 1
    current = 1

    for i in range(n+1):
        current += i

    return current


print(fibo_iter(5))
print(fibo_iter(10))


def facto_rec(n):
    if n == 0:
        return 1

    return n * facto_rec(n-1)


print(facto_rec(5))


def facto_iter(n):
    count = 1

    for i in range(1, n+1):
        count *= i

    return count


print(facto_iter(8))


def f91(n: int):
    if n > 100:
        return n - 10
    return f91(f91(n+11))
    # Conjecturation de f91(n) avec n <= 101, le résultat sera toujours 91


def f91_detail(n, k=1):
    result = n
    for i in range(k):
        result = f91(result)

    return result


print(f91_detail(102, 3))
print(f91(f91(f91(102))))


def F(n: int):
    if n == 0:
        return 1
    elif n > 0:
        return n - M(F(n-1))


def M(n: int):
    if n == 0:
        return 0
    elif n > 0:
        return n - F(M(n-1))


print(F(9))
print(M(9))


def syracuse(u: int):
    print(u)
    if u != 1:
        if u % 2 == 0:
            syracuse(u/2)
        else:
            syracuse(3 * u + 1)


# syracuse(5)
# syracuse(548)


def duree_vol(u: int):
    if u == 1:
        return 0
    if u % 2 == 0:
        return duree_vol(u / 2)+1
    else:
        return duree_vol(3 * u + 1)+1


def dv(u: int):
    c = u
    highest = 0
    counter = 0
    while c != 1:
        counter += 1
        if c % 2 == 0:
            c /= 2
        else:
            c = c * 3 + 1

        if highest < c:
            highest = c

    print(highest)

    return counter


print(duree_vol(5))
print(dv(674))


def altitude(u: int):
    if u == 1:
        return 0

    if u % 2 == 0:
        new_value = altitude(u / 2)
    else:
        new_value = altitude(u * 3 + 1)
    return new_value if new_value > u else u


print(altitude(674))
