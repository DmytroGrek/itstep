# Розширте попередню програму, так щоб квадрат пульсував (збільшувався у розмірі і поступово
# повертався в попередній розмір). Код помістіть в окрему папку pygame_pulsar.
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame_pulsar')

x = 250
y = 250
width = 50
height = 50

run = True
flag = True
while run:
    pygame.time.delay(30)
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            run = False

    if flag:
        width += 1
        height += 1
    else:
        width -= 1
        height -= 1
    if width == 255:
        flag = False
    if width == 50:
        flag = True

    win.fill((0, 0, 255))
    pygame.draw.rect(win, (255, 255, 0), (x - width // 2, y - height // 2, width, height))
    pygame.display.update()
pygame.quit()
