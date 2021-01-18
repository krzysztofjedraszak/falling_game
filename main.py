import random

import pgzrun

klatka = 0
stan_gry = 0
anvils = []
stars = []
fireballs = []
hearts = []
level = 0
zycia = 3
punkty = 0

gracz = Actor("p1_stand", (400, 484))

y1_min = -2100
y2_max = -100

for _ in range(12):
    anvil = Actor("anvil", (random.randint(0, 800), random.randint(y1_min, y2_max)))
    anvils.append(anvil)

for _ in range(7):
    star = Actor("star", (random.randint(0, 800), random.randint(y1_min, y2_max)))
    stars.append(star)

for _ in range(5):
    fireball = Actor("fireball", (random.randint(0, 800), random.randint(y1_min, y2_max)))
    fireballs.append(fireball)

for i in range(3):
    heart = Actor("heart", (30 + 53 * i, 28))
    hearts.append(heart)


def dodanie_obiektow():
    global punkty
    global level
    if punkty >= 50 and punkty < 100:
        if level == 0:
            for _ in range(2):
                anvil = Actor("anvil", (random.randint(0, 800), random.randint(y1_min, y2_max)))
                anvils.append(anvil)
            level += 1

    if punkty >= 100 and punkty < 150:
        if level == 1:
            for _ in range(3):
                fireball = Actor("fireball", (random.randint(0, 800), random.randint(y1_min, y2_max)))
                fireballs.append(fireball)
            level += 1

    if punkty >= 150 and punkty < 200:
        if level == 2:
            for _ in range(2):
                anvil = Actor("anvil", (random.randint(0, 800), random.randint(y1_min, y2_max)))
                anvils.append(anvil)
            level += 1

    if punkty >= 200 and punkty < 250:
        if level == 3:
            for _ in range(2):
                anvil = Actor("anvil", (random.randint(0, 800), random.randint(y1_min, y2_max)))
                anvils.append(anvil)
            level += 1

    if punkty >= 300:
        if level == 4:
            for _ in range(2):
                anvil = Actor("anvil", (random.randint(0, 800), random.randint(y1_min, y2_max)))
                anvils.append(anvil)
            level += 1


def reset():
    global zycia
    global punkty
    global klatka
    global stan_gry
    zycia = 3
    punkty = 0
    klatka = 0
    stan_gry = 0


def dodanie_zyc():
    global stan_gry
    if stan_gry == "q":
        for i in range(3):
            heart = Actor("heart", (30 + 53 * i, 28))
            hearts.append(heart)


def draw():
    global stan_gry
    global zycia
    global punkty

    screen.clear()
    screen.fill('#ebe591')
    for i in range((screen.width // 70) + 1):
        screen.blit("castle", (i * 70, screen.height - 70))

    gracz.draw()

    for i in anvils:
        i.draw()
    for i in stars:
        i.draw()
    for i in fireballs:
        i.draw()
    for i in hearts:
        i.draw()

    screen.draw.text(f"Punkty: {punkty}", center=(650, 28), color="orange", fontsize=60)

    if stan_gry == 0:
        screen.draw.text("Wcisnij ENTER aby rozpoczac gre", center=(screen.width / 2, screen.height / 2),
                         color="orange", fontsize=60)

    if zycia == 0:
        stan_gry = "q"
        screen.draw.text("Przegrales :( Koniec Gry", center=(screen.width / 2, screen.height / 2 - 30), color="orange",
                         fontsize=60)
        screen.draw.text("Wcisnij ENTER aby zagrac jeszcze raz", center=(screen.width / 2, screen.height / 2 + 30),
                         color="orange", fontsize=60)
        if keyboard.RETURN:
            dodanie_zyc()
            reset()


def update():
    global klatka
    global stan_gry

    if keyboard.RETURN:
        if stan_gry == 0:
            stan_gry = 1

    if stan_gry == 1:
        szybkosc = 6
        if keyboard.RIGHT or keyboard.LEFT:
            if keyboard.RIGHT:
                gracz.left += szybkosc

            if keyboard.LEFT:
                gracz.left -= szybkosc

            if keyboard.SPACE and keyboard.LEFT:
                gracz.left -= 2 * szybkosc

            if keyboard.SPACE and keyboard.RIGHT:
                gracz.left += 2 * szybkosc

            animacja_gracza()

        if gracz.right < 0:
            gracz.left = screen.width

        if gracz.left > screen.width:
            gracz.right = 0

        spadanie_przeszkod()
        detektor_kolizji()


def animacja_gracza():
    global klatka
    if stan_gry == 1:
        for i in range(1, 10):
            if klatka == 0:
                gracz.image = "p1_walk01"

            elif klatka == i:
                gracz.image = f"p1_walk0{i}"
            # elif klatka == 1:
            #     gracz.image = f"p1_walk02"
            # elif klatka == 2:
            #     gracz.image = f"p1_walk03"
            # elif klatka == 3:
            #     gracz.image = f"p1_walk04"
            # elif klatka == 4:
            #     gracz.image = f"p1_walk05"
            # elif klatka == 5:
            #     gracz.image = f"p1_walk06"
            # elif klatka == 6:
            #     gracz.image = f"p1_walk07"
            # elif klatka == 7:
            #     gracz.image = f"p1_walk08"
            # elif klatka == 8:
            #     gracz.image = f"p1_walk09"
            elif klatka == 9:
                gracz.image = "p1_walk10"
            elif klatka == 10:
                gracz.image = "p1_walk11"

    klatka += 1
    if klatka == 11:
        klatka = 0


def spadanie_przeszkod():
    global y1_min
    global y2_max

    for anvil in anvils:
        anvil.y += 6
        if anvil.y >= 600:
            anvil.y = random.randint(y1_min, y2_max)
            anvil.x = random.randint(0, 800)

    for star in stars:
        star.y += 5
        if star.y >= 600:
            star.y = random.randint(y1_min, y2_max)
            star.x = random.randint(0, 800)

    for fireball in fireballs:
        fireball.y += 8
        if fireball.y >= 600:
            fireball.y = random.randint(y1_min, y2_max)
            fireball.x = random.randint(0, 800)


def detektor_kolizji():
    global zycia
    global punkty
    global y1_min
    global y2_max

    for i in anvils:
        if gracz.colliderect(i):
            if zycia >= 1:
                zycia -= 1
                hearts.pop()
                i.x = random.randint(0, 800)
                i.y = random.randint(y1_min, y2_max)

    for i in stars:
        if gracz.colliderect(i):
            punkty += 10
            i.x = random.randint(0, 800)
            i.y = random.randint(y1_min, y2_max)

    for i in fireballs:
        if gracz.colliderect(i):
            if zycia >= 1:
                zycia -= 1
                punkty -= 5
                hearts.pop()
                i.x = random.randint(0, 800)
                i.y = random.randint(y1_min, y2_max)


pgzrun.go()
