import pygame,sys,random

pygame.init()

def drawArena(color1, color2, screen, Window_width, Window_height, LineThickness):
    screen.fill(color2)

    pygame.draw.rect(screen, color1, ((0,0),(Window_width,Window_height)),LineThickness)



def displayScore(screen, score1, score2, color1, Font):
    p1Score = Font.render('%s' %(score1), True, color1)
    p2Score = Font.render('%s' %(score2), True, color1)
    screen.blit(p1Score,[50,25])
    screen.blit(p2Score,[225,25])
