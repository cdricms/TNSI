def convertir(l: list):

    result = 0
    for i in range(len(l)):
        if l[i] == 1:
            print(i)
            result += 2**i
            print(result)

    return result


print(convertir([1, 0, 1, 0, 0, 1, 1]))
