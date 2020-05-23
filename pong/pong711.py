# 7.1.1 Installation and basics with pygame

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

red = pygame.Color('red')
screen.fill(red)

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

quit()
