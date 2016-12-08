import pygame

pygame.init()

def drawPaddle(screen, color1, paddle, Window_height, LineThickness):
    if paddle.bottom > Window_height - LineThickness:
        paddle.bottom = Window_height - LineThickness
    elif paddle.top < LineThickness:
        paddle.top = LineThickness
    pygame.draw.rect(screen, color1, paddle)

def artificialIntelligence(ball, ballDirY, paddle2):
    if ballDirY == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -= 1
    return paddle2
