#1 - GG
unites = []
for _ in range(25):
    unites.append(1)
print(unites)

#1 - 2
unites = [1 for _ in range(25)]
print(unites)

#2 - 1
tab = []
for _ in range(100):
    tab.append("informatique")
print(tab)

#2 - 2
tab = ["informatique" for _ in range(100)]
print(tab)

#3 - 1
multiples_11 = [x for x in range(50) if x % 11 == 0]
print(multiples_11)

#4 - 1
table = [f"9 x {x} = {9*x}" for x in range(20)]
print(table)

#5 - 1
secondes = [17.5, 19.2, 21, 20.3, 19.7]
hours = [x * 3600 for x in secondes]
print(hours)

#6 - 1
temp_celcius = [17.5, 19.2, 21, 20.3, 19.7]
temp_fahr = [x * 9/5 + 32 for x in temp_celcius]
print(temp_fahr)

#7 - 1
l = [2, 15, 14, 10, 15, 21, 18]
decode = [chr(x+96) for x in l]
print(decode)

#8 - 1
L = [1, 4, 2, 7, 1, 9, 0, 3, 4, 6, 6, 6, 8, 3]
superieurs = [x for x in L if x > 5]
print(superieurs)

#9 - 1
pairs = [x for x in range(100, 150) if x % 2 == 0]
print(pairs)

#10 - 1
bissextile = [x for x in range(1500, 2031) if (
    x % 400 == 0 or x % 4 == 0) and x % 100 != 0]
print(bissextile)

#11 - 1
petits_mots = ["girafe", "gnou", "antilope", "lion", "autruche"]
p = [x for x in petits_mots if len(x) <= 5]
print(p)


#12 - 1
L = ["alice", "tom", "pierre", "alain", "chloé"]
voyelles = [97, 101, 105, 111, 117, 121]
consonnes = [chr(x) for x in range(97, 123) if x not in voyelles]
prenom_consonne = [x.capitalize() for x in L if x[0] in consonnes]
print(prenom_consonne)

#13 - 1
L = [
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)],
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)],
    [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)],
    [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)],
    [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
]
