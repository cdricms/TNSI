def occurrence_max(chaine):
    dico = {}

    for s in chaine:
        if s != " ":
            if s not in dico:
                dico[s] = 0
            dico[s] += 1

    print(dico)
    highest = 0
    maxi = None
    for (key, value) in dico.items():
        if value > highest:
            highest = value
            maxi = key

    return maxi


ch = "je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique"

print(occurrence_max(ch))
