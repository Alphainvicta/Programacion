import sys, pygame
import math

pygame.init()

size = width, height = 1920, 1080
spd = 3
speed = [spd, 0]
c = 1
black = 0, 0, 0
screen = pygame.display.set_mode(size)

s = pygame.image.load("./sprites/feliz1.png")
s = pygame.transform.scale(s, (160, 160))
srect = s.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    srect = srect.move(speed)
    if srect.right > width and c == 1:
        speed = [0, spd]
        c += 1
    if srect.bottom > height and c == 2:
        speed = [-spd, 0]
        c += 1
    if srect.left < 0 and c == 3:
        speed = [0, -spd]
        c += 1
    if srect.top < 0 and c == 4:
        speed = [spd, 0]
        c += 1

    if c == 5 and srect.right >= (width / 2 + 80):
        speed = [0, spd]
        if srect.bottom > height + 160:
            srect.top = -160
            c += 1

    if c == 6 and srect.bottom >= (height / 2 + 80):
        speed = [spd, 0]
        if srect.right > width + 160:
            srect.left = -160
            c += 1

    if c == 7 and srect.right >= (width / 2 + 80):
        angle = 0.0
        x = srect.x
        y = height / 2 - 80
        speed = [0, 0]
        c += 1

    if c == 8:
        srect.x = 450 * math.cos(angle) + x
        srect.y = 450 * math.sin(angle) + y
        angle += 0.01

    screen.fill(black)
    screen.blit(s, srect)
    pygame.display.flip()
