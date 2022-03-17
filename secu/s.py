def chiffre_xor(message, key):
    """
    Entrée(s) : message, key de type str
    Sortie: type list de int
    """
    c = []
    n = len(message)
    m = len(key)
    j = 0
    for i in range(n):
        c.append(ord(message[i]) ^ ord(key[j]))
        j = (j+1) % m
    return c


def chiffre_xor_v2(msg, key):
    if (isinstance(msg, str)):
        msg = chiffre_xor(msg, key)
    a = ""
    k = 0
    for i in msg:
        a += chr(i ^ ord(key[k]))
        k = (k+1) % len(key)

    return a


def ceasar(txt: str, key: int = 13):
    dico = {chr(i+65): chr((i+key) % 26+65) for i in range(26)}

    crpt = ""
    for i in txt:
        if (x := dico.get(i.upper())):
            crpt += x
        else:
            crpt += i

    return crpt


message = "Bonjour, comment allez-vous ?"
cle = "mystère"
a = chiffre_xor(message, cle)
b = chiffre_xor_v2(a, cle)
print(a)
print(b)
print(chiffre_xor_v2(b, cle))

print(ceasar(message, 15))


def ch_RSA_char(c: str, pub: tuple):
    return chr(ord(c)**pub[0] % pub[1]), pub


print(ch_RSA_char("c", (41, 437)))


def ch_RSA_charp(c: int, priv: tuple):
    return chr(ord(c)**priv[0] % priv[1]), priv


def dp(t: str, pr: tuple):
    a = ""
    for i in t:
        a += ch_RSA_charp(i, pr)[0]

    return a


p = dp("coucou", (103, 697))
print(p)


def d(t: str, p: tuple):
    a = ""
    for i in t:
        a += ch_RSA_char(i, p)[0]

    return a


print(d(p, (87, 697)))
