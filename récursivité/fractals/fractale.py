import turtle as tt

HEIGHT = 1920
WIDTH = 1080

tt.setup(WIDTH, HEIGHT)


def init(x=0, y=0, direction=0):
    tt.setpos(x, y)
    tt.seth(direction)


init()


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


tt.tracer(1000)
triangle(100)
tt.update()
tt.Screen().exitonclick()
