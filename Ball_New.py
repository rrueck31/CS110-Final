import pygame

pygame.init()

def drawBall(ball, screen, color):
    pygame.draw.rect(screen, color, ball)

def moveBall(ball,ballDirX,ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball
