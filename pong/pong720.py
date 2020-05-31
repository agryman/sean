# 7.2 The Pong Game

import pygame

pygame.init()

BORDER = 10
WIDTH = 800
HEIGHT = 400

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)

pygame.draw.rect(screen, WHITE,
                 pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, WHITE,
                 pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, WHITE,
                 pygame.Rect(0, HEIGHT - BORDER,
                             WIDTH, BORDER))

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
pygame.quit()
