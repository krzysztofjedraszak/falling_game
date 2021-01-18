import pgzrun
import random

klatka = 0
stan_gry = 0
anvils=[]
stars=[]
fireballs=[]
hearts=[]
level=0
zycia=3
punkty=0

gracz = Actor("p1_stand", (400, 484))

def draw():
    global stan_gry
    global zycia
    global punkty

    screen.clear()
    screen.fill('#ebe591')
    for i in range((screen.width // 70) + 1):
        screen.blit("castle", (i * 70, screen.height - 70))

    gracz.draw()

    screen.draw.text(f"Punkty: {punkty}", center=(650 , 28), color="orange",fontsize=60)

    if stan_gry == 0:
        screen.draw.text("Wcisnij ENTER aby rozpoczac gre", center=(screen.width / 2, screen.height / 2),color="orange", fontsize=60)


def update():
    global klatka
    global stan_gry

    if keyboard.RETURN:
        if stan_gry == 0:
            stan_gry = 1

    if stan_gry==1:
        szybkosc=6
        if keyboard.RIGHT or keyboard.LEFT:
            if keyboard.RIGHT:
                gracz.left += szybkosc

            if keyboard.LEFT:
                gracz.left -= szybkosc

            if keyboard.SPACE and keyboard.LEFT:
                gracz.left -= 2*szybkosc

            if keyboard.SPACE and keyboard.RIGHT:
                gracz.left += 2*szybkosc

            animacja_gracza()

        if gracz.right < 0:
            gracz.left = screen.width

        if gracz.left > screen.width:
            gracz.right = 0

        spadanie_przeszkod()
        detektor_kolizji()







































































pgzrun.go()