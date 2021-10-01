import sys, pygame
import math

pygame.init()

size = width, height = 1920, 1080
spd = 1
ang = 0.01
speed = [0, 0]
o1 = 0
o2 = 0
o3 = 0
black = 0, 0, 0
screen = pygame.display.set_mode(size)

s = pygame.image.load("./sprites/feliz1.png")
s = pygame.transform.scale(s, (160, 160))
srect = s.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
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
            if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                srect.x = 0
                srect.y = 0
                speed = [spd, 0]
                o1 = 1
                o2 = 0
                c1 = 0
                o3 = 0
            if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                srect.x = width / 2 - 80
                srect.y = 0
                speed = [0, spd]
                o2 = 1
                c2 = 0
                o1 = 0
                o3 = 0
            if event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                srect.x = width / 2 - 80
                srect.y = 0
                speed = [0, spd]
                o1 = 0
                o2 = 0
                o3 = 1
                c3 = 0

    srect = srect.move(speed)

    if o1 == 1:
        if srect.right > width and c1 == 0:
            speed = [0, spd]
            c1 += 1
        if srect.bottom > height and c1 == 1:
            speed = [-spd, 0]
            c1 += 1
        if srect.left < 0 and c1 == 2:
            speed = [0, -spd]
            c1 += 1
        if srect.top < 0 and c1 == 3:
            speed = [spd, 0]
            c1 = 0

    if o2 == 1:
        if c2 == 0 and srect.right >= (width / 2 + 80):
            speed = [0, spd]
            if srect.bottom > height + 160:
                srect.left = -160
                srect.bottom = height / 2 + 80
                c2 += 1

        if c2 == 1 and srect.bottom >= (height / 2 + 80):
            speed = [spd, 0]
            if srect.right > width + 160:
                srect.x = width / 2 - 80
                srect.top = -160
                speed = [0, spd]
                c2 = 0

    if o3 == 1:
        if c3 == 0 and srect.right >= (width / 2 + 80):
            angle = 0.0
            radio = width / 4
            x = srect.x
            y = height / 2 - 80
            speed = [0, 0]
            c3 += 1

        if c3 == 1:
            srect.x = radio * math.cos(angle) + x
            srect.y = radio * math.sin(angle) + y
            angle += ang

    screen.fill(black)
    screen.blit(s, srect)
    pygame.display.flip()
