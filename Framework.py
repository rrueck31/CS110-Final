import pygame
from Paddles import *

pygame.init()

BLACK = [0,0,0]
WHITE = [255,255,255]

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("PONG")

done = False
clock = pygame.time.Clock()
key = pygame.key.get_pressed()
stage = "1"

p1 = Paddle((100,175),(25,150))
p2 = Paddle((600,175),(25,150))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    
    #Drawing
    while stage == "1":

        font = pygame.font.SysFont('OCR A Extended', 36, True, False)
        text = font.render("PONG", True, WHITE)
        text2 = font.render("PRESS ENTER TO PLAY", True, WHITE)

        screen.blit(text,[250, 0])
        screen.blit(text2, [100,400])

        if key[pygame.K_RETURN]:
            stage = "2"

        pygame.display.flip()
                    

    while stage == "2":
        screen.fill(BLACK)

        Paddle.draw(p1,screen)
        Paddle.draw(p2,screen)
        Paddle.key_press(p1)

        pygame.display.flip()

                    


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
