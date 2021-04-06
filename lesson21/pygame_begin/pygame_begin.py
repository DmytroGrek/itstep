# Вам потрібно розібратися з основами бібліотеки pygame (стаття що допоможе розібратися з бібліотекою
# вище) та побудувати першу маленьку сцену. Вам потрібно відтворити сцену довільного розміру з синім
# фоном та відобразити в центрі квадрат жовтого кольору. Код помістіть в окрему папку pygame_begin.
# Код можете розбивати на довільну кількість файлів.
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame_begin')
x = 225
y = 225
width = 50
height = 50

run = True
while run:
    pygame.time.delay(50)
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
