import json
from os import read
import sys, pygame

pygame.init()

r = open("Parcial2\pnovelas\synapse.json")
data = json.load(r)

black = 0, 0, 0
size = width, height = 500, 1000
screen = pygame.display.set_mode(size)


def actos(text, background, c):
    if c == 14:
        rr = open(data["fin"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["fin"]["imagen"])

    if c == 13:
        rr = open(data["acto13"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto13"]["imagen"])
        c += 1

    if c == 12:
        rr = open(data["acto12"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto12"]["imagen"])
        c += 1

    if c == 11:
        rr = open(data["acto11"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto11"]["imagen"])
        c += 1

    if c == 10:
        rr = open(data["acto10"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto10"]["imagen"])
        c += 1

    if c == 9:
        rr = open(data["acto9"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto9"]["imagen"])
        c += 1

    if c == 8:
        rr = open(data["acto8"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto8"]["imagen"])
        c += 1

    if c == 7:
        rr = open(data["acto7"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto7"]["imagen"])
        c += 1

    if c == 6:
        rr = open(data["acto6"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto6"]["imagen"])
        c += 1

    if c == 5:
        rr = open(data["acto5"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto5"]["imagen"])
        c += 1

    if c == 4:
        rr = open(data["acto4"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto4"]["imagen"])
        c += 1

    if c == 3:
        rr = open(data["acto3"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto3"]["imagen"])
        c += 1

    if c == 2:
        rr = open(data["acto2"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto2"]["imagen"])
        c += 1

    if c == 1:
        rr = open(data["acto1"]["texto"])
        text = rr.read()
        rr.close()
        background = pygame.image.load(data["acto1"]["imagen"])
        c += 1

    return text, background, c


def opciones(text, background, c):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_SPACE:
        text, background, c = actos(text, background, c)
    return text, background, c


def blit_text(surface, text, pos, font, color=pygame.Color("white")):
    words = [
        word.split(" ") for word in text.splitlines()
    ]  # 2D array where each row is a list of words.
    space = font.size(" ")[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width - 10:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


c = 1

rr = open(data["inicio"]["texto"])
text = rr.read()
rr.close()

background = pygame.image.load(data["inicio"]["imagen"])
font = pygame.font.Font(None, 30)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            text, background, c = opciones(text, background, c)

    screen.fill(black)
    screen.blit(background, (0, 0))
    blit_text(screen, text, (10, 510), font)
    pygame.display.flip()
