import pygame,sys,random

pygame.init()

FPS = 75

def showStartScreen(screen, clock, FontSize, color1, color2):
    titleFont = pygame.font.SysFont('OCR A Extended', FontSize)
    subFont = pygame.font.SysFont('OCR A Extended', 16)
    title1 = titleFont.render("PONG", True, color1)
    title2 = subFont.render("Press any key to play", True, color1)

    Title = True
    
    while Title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                pygame.event.get()
                Title = False
            screen.fill(color2)
            screen.blit(title1, [100, 25])
            screen.blit(title2, [50, 325])


        pygame.display.update()
        clock.tick(FPS)

def showWinningScreen(screen, clock, FontSize, color1, color2):
    titleFont = pygame.font.SysFont('OCR A Extended', FontSize)
    subFont = pygame.font.SysFont('OCR A Extended', 16)
    text1 = titleFont.render("YOU WIN!", True, color1)

    gameOver = True

    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill(color2)
            screen.blit(text1, [70, 25])

        pygame.display.update()
        clock.tick(FPS)


def showLosingScreen(screen, clock, FontSize, color1, color2):
    titleFont = pygame.font.SysFont('OCR A Extended', FontSize)
    text1 = titleFont.render("YOU LOSE", True, color1)

    gameOver = True

    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill(color2)
            screen.blit(text1, [70, 25])

        pygame.display.update()
        clock.tick(FPS)
