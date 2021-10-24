import json
import sys, pygame

pygame.init()

r = open("Parcial2\pnovelas\synapse.json")
data = json.load(r)

background = pygame.image.load(data["inicio"]["imagen"])
rr = open(data["inicio"]["texto"])
text = rr.read()
se = "inicio"
rr.close()

black = 0, 0, 0
size = width, height = 500, 700
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 30)


def opciones(text, background, se):
    for i in range(len(data[se]["opciones"])):
        if event.key == data[se]["opciones"][i]:
            se = data[se][str(event.key)]
            break
    text, background, se = secciona(text, background, se)
    return text, background, se


def secciona(text, background, se):
    background = pygame.image.load(data[se]["imagen"])
    rr = open(data[se]["texto"])
    text = rr.read()
    rr.close()
    return text, background, se


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


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            text, background, se = opciones(text, background, se)

    screen.fill(black)
    screen.blit(background, (0, 0))
    blit_text(screen, text, (10, 510), font)
    pygame.display.flip()
