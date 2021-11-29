def ack(m: int, n: int):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, n)
    else:
        return ack(m-1, ack(m, n-1))


def mystere(n):
    if n < 10:
        return n
    else:
        return n % 10 + mystere(n/10)


print(mystere(5048))
