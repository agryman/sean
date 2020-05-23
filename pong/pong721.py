# 7.2.1 The Ball class

import pygame

pygame.init()

BORDER = 10
WIDTH = 800
HEIGHT = 400
VELOCITY = -4

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

class Ball:

    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour,
                           (self.x, self.y), self.RADIUS)

    def update(self):

        # compute next position of ball at current velocity
        newx = self.x + self.vx
        newy = self.y + self.vy

        #detect vertical bounce
        if newy + Ball.RADIUS > HEIGHT - BORDER\
                or newy - Ball.RADIUS < BORDER:
            self.vy = -self.vy
        # detect horizontal bounce
        elif newx - Ball.RADIUS < BORDER:
            self.vx = -self.vx
        else:
            # hide the ball
            self.show(BLACK)

            # move the ball
            self.x = newx
            self.y = newy

            # show the ball
            self.show(WHITE)

ball = Ball(WIDTH - Ball.RADIUS, HEIGHT // 2,
            VELOCITY, 0)
ball.show(WHITE)

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    ball.update()
    pygame.display.flip()
quit()
