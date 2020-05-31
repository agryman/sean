# 7.2.2 The Paddle class

import pygame

pygame.init()

BORDER = 10
WIDTH = 800
HEIGHT = 400
VELOCITY = 4

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
        self.moving = False

    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour,
                           (self.x, self.y), self.RADIUS)

    def update(self):

        if not self.moving:
            return

        # compute next position of ball at current velocity
        newx = self.x + self.vx
        newy = self.y + self.vy

        #detect vertical bounce
        if newy + Ball.RADIUS > HEIGHT - BORDER \
                or newy - Ball.RADIUS < BORDER:
            self.vy = -self.vy
        # detect horizontal bounce
        elif newx - Ball.RADIUS < BORDER:
            self.vx = -self.vx
        elif newx + Ball.RADIUS >= WIDTH - Paddle.WIDTH \
            and abs(newy - paddle.y) <= Paddle.HEIGHT // 2:
            self.vx = -self.vx
        else:
            # hide the ball
            self.show(BLACK)

            # move the ball
            self.x = newx
            self.y = newy

            # show the ball
            self.show(WHITE)

class Paddle:
    WIDTH = 10
    HEIGHT = 80

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        global screen
        pygame.draw.rect(screen, colour,
                         pygame.Rect(WIDTH - self.WIDTH,
                                     self.y - self.HEIGHT // 2,
                                     self.WIDTH,
                                     self.HEIGHT))

    def update(self):

        newy = pygame.mouse.get_pos()[1]

        if newy - self.HEIGHT // 2 >= BORDER \
            and newy + self.HEIGHT // 2 <= HEIGHT - BORDER:


            # hide the paddle
            self.show(BLACK)

            #move the paddle to the mouse position
            self.y = newy

            # show the paddle
            self.show(WHITE)

# create the paddle in the middle of the screen
paddle = Paddle(HEIGHT // 2)

# show the paddle
paddle.show(WHITE)

# create the ball in the middle of the screen to the left of the paddle
ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH, HEIGHT // 2,
            -VELOCITY, -VELOCITY)
ball.show(WHITE)

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    elif e.type == pygame.MOUSEBUTTONDOWN:
        ball.moving = not ball.moving
    ball.update()
    paddle.update()
    pygame.display.flip()

pygame.quit()
