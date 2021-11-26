import sys, pygame

pygame.init()

size = width, height = 800, 800
black = 0, 0, 0
latav = pygame.image.load("./parcial3/lata/latav.png")
lata = pygame.image.load("./parcial3/lata/lata.png")

surf = pygame.Surface((190, 330))
surf.fill((0, 0, 0))
y = 100
p = 0
c = 0

screen = pygame.display.set_mode(size)

font = pygame.font.Font(None, 50)
text = font.render(("Porcentaje actual: "), 0, (255, 255, 255))
textp = font.render((str(p)), 0, (255, 255, 255))


def con(y, p, c):
    if event.key == pygame.K_KP_PLUS:
        if y > -230:
            y -= 1
            c += 1
    if event.key == pygame.K_KP_MINUS:
        if y < 100:
            y += 1
            c -= 1
    if c != 0:
        p = round((c * 100) / 330)
    if c == 0:
        p = 0
    return y, p, c


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            y, p, c = con(y, p, c)

    screen.fill(black)
    screen.blit(lata, (300, 100))
    screen.blit(surf, (300, y))
    screen.blit(latav, (300, 100))
    screen.blit(text, (200, 600))
    textp = font.render((str(p)), 0, (255, 255, 255))
    screen.blit(textp, (550, 600))
    pygame.display.flip()
