import turtle as tt

HEIGHT = 1920
WIDTH = 1080

tt.setup(WIDTH, HEIGHT)


def init(x=0, y=0, direction=0):
    tt.setpos(x, y)
    tt.seth(direction)


def koch(etape, longueur):
    if etape == 0:
        tt.fd(longueur)
    else:
        koch(etape-1, longueur/3)
        tt.left(60)
        koch(etape-1, longueur/3)
        tt.right(120)
        koch(etape-1, longueur/3)
        tt.left(60)
        koch(etape-1, longueur/3)


def flocon(etape, longueur):
    if etape == 0:
        for x in range(3):
            koch(etape-1, longueur/3)
            tt.rt(120)
    else:
        for x in range(3):
            koch(etape-1, longueur/3)
            tt.left(60)
            koch(etape-1, longueur/3)
            tt.right(120)
            koch(etape-1, longueur/3)
            tt.left(60)
            koch(etape-1, longueur/3)
            tt.rt(120)


def triangle(longueur):
    tt.fillcolor('blue')  # couleur pour colorier
    tt.begin_fill()  # pour colorier la suite
    for i in range(3):
        tt.forward(longueur)
        tt.left(120)
        tt.end_fill()  # on finit le coloriage


def init_arbre(etape, longueur):

    init(direction=90)

    def arbre(etape, longueur):
        if etape == 0:
            tt.fd(longueur)
        else:
            arbre(etape-1, longueur)
            tt.left(45)
            arbre(etape-1, longueur/2)
            tt.left(-180)
            tt.fd(longueur/2)
            tt.left(90)
            arbre(etape-1, longueur/2)
            tt.left(180)
            tt.fd(longueur/2)
            tt.left(-90-45)

    arbre(etape, longueur)


def init_pyt(etape, longueur, alpha):
    init(direction=90)

    def arbre_pythagore(etape, longueur, alpha):
        if etape == 0:
            tt.fillcolor("green")
            tt.begin_fill()
            for i in range(4):
                tt.fd(longueur)
                tt.rt(90)
            tt.end_fill()
        else:
            arbre_pythagore(etape-1, longueur, alpha)
            tt.fd(longueur)
            tt.left(45)
            arbre_pythagore(etape-1, longueur/2, alpha)
            tt.left(180+45)
            tt.fd(longueur)
            tt.left(90)
            tt.left(45)
            arbre_pythagore(etape-1, longueur/2, alpha)

    arbre_pythagore(etape, longueur, alpha)


tt.tracer(1000)
init_pyt(1, 200, 45)
tt.update()
tt.Screen().exitonclick()
