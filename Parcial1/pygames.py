import sys, pygame
import math

pygame.init()

width = int(input("introduce el ancho de la pantalla: "))
print("")
height = int(input("introduce el alto de la pantalla: "))

size = width, height
spd = 1
speed = [0, 0]
ang = 0.01
angulo = 0.0
o = 0
black = 0, 0, 0
screen = pygame.display.set_mode(size)

s = pygame.image.load("./sprites/feliz1.png")
s = pygame.transform.scale(s, (160, 160))
srect = s.get_rect()


def teclasv(spd, ang):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_KP_0:
        spd = 1
        ang = 0.01
    if event.key == pygame.K_KP_PLUS:
        spd += 1
        ang += 0.01
    if event.key == pygame.K_KP_MINUS:
        if spd > 1:
            spd -= 1
        if ang > 0.01:
            ang -= 0.01
    return spd, ang


def opciones(srect, speed, angulo, o):
    if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
        srect.x = 0
        srect.y = 0
        speed = [spd, 0]
        o = 1

    if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
        srect.x = width / 2 - 80
        srect.y = 0
        speed = [0, spd]
        o = 2

    if event.key == pygame.K_3 or event.key == pygame.K_KP_3:
        srect.x = width / 2 - 80
        srect.y = 0
        speed = [0, 0]
        angulo = 0.0
        o = 3

    return srect, speed, angulo, o


def rodear(speed):
    if srect.right > width:
        speed = [0, spd]

    if srect.bottom > height:
        speed = [-spd, 0]

    if srect.left < 0:
        speed = [0, -spd]

    if srect.top < 0:
        speed = [spd, 0]
        if srect.right > width:
            speed = [0, spd]

    return speed


def cruz(speed):
    if srect.bottom > height + 160:
        srect.left = -160
        srect.bottom = height / 2 + 80
        speed = [spd, 0]

    if srect.right > width + 160:
        srect.x = width / 2 - 80
        srect.top = -160
        speed = [0, spd]

    return speed


def circulo(srect, angulo):
    srect.x = (height / 2 - 80) * math.cos(angulo) + (width / 2 - 80)
    srect.y = (height / 2 - 80) * math.sin(angulo) + (height / 2 - 80)
    angulo += ang
    return srect, angulo


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            spd, ang = teclasv(spd, ang)
            srect, speed, angulo, o = opciones(srect, speed, angulo, o)

    srect = srect.move(speed)

    if o == 1:
        speed = rodear(speed)

    if o == 2:
        speed = cruz(speed)

    if o == 3:
        srect, angulo = circulo(srect, angulo)

    screen.fill(black)
    screen.blit(s, srect)
    pygame.display.flip()
