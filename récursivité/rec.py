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
