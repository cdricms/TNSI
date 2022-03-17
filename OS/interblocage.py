from threading import Thread
from time import sleep

compteur = 0  # Variable globale
limite = 100


def calcul():
    global compteur
    for c in range(limite):
        temp = compteur
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        compteur = temp + 1


calcul()
print(compteur)


compteur = 0
for i in range(4):  # Lance en parallèle 4 exécutions du calcul
    p = Thread(target=calcul)
    p.start()  # Lance calcul dans un processus léger à part
    sleep(0.01)


print(compteur)
