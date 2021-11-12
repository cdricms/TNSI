def pow_o(a: int, n: int):
    if n == 0:
        return 1

    if n % 2 == 0:
        return pow_o(a*a, n/2)
    else:
        return a * pow_o(a, n-1)


print(pow_o(2, 5000))
