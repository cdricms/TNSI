def calcul(n):
    print(n)

    if n >= 1:
        if n % 2 == 0:
            return calcul(n / 2)
        else:
            return calcul(n*3+1)

    return n


print(calcul(7))
