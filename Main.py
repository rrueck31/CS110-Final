import pygame, sys, random, Arena, Ball_New, Game_Checks, Game_State, Paddles_New

FPS = 75

Window_height = 400
Window_width = 300

LineThickness = 10
PaddleSize = 50
PaddleOffset = 20

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((Window_width,Window_height))
pygame.display.set_caption("PONG")

FontSize = 36
Font = pygame.font.SysFont('OCR A Extended', FontSize)

def main():
    Game_State.showStartScreen(screen, clock, FontSize, WHITE, BLACK)
    
    ballx = Window_width/2 - LineThickness/2
    bally = Window_height/2 - LineThickness/2
    p1POS = (Window_height - PaddleSize)/2
    score1 = 0
    p2POS = (Window_height - PaddleSize)/2
    score2 = 0

    ballDirX = -1
    ballDirY = -1

    paddle1 = pygame.Rect(PaddleOffset, p1POS, LineThickness, PaddleSize)
    paddle2 = pygame.Rect(Window_width - PaddleOffset - LineThickness, p2POS, LineThickness, PaddleSize)
    ball = pygame.Rect(ballx, bally, LineThickness, LineThickness)

    
    Arena.drawArena(WHITE, BLACK, screen, Window_width, Window_height, LineThickness)
    Paddles_New.drawPaddle(screen, WHITE, paddle1, Window_height, LineThickness)
    Paddles_New.drawPaddle(screen, WHITE, paddle2, Window_height, LineThickness)
    Ball_New.drawBall(ball, screen, WHITE)

    
    running = True

    pygame.mouse.set_visible(0)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = event.pos
                paddle1.y = mouseY
                

        Arena.drawArena(WHITE, BLACK, screen, Window_width, Window_height, LineThickness)
        Paddles_New.drawPaddle(screen, WHITE, paddle1, Window_height, LineThickness)
        Paddles_New.drawPaddle(screen, WHITE, paddle2, Window_height, LineThickness)
        Ball_New.drawBall(ball, screen, WHITE)

        ball = Ball_New.moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = Game_Checks.checkEdgeCollision(ball, ballDirX, ballDirY, Window_height, Window_width, LineThickness)
        score1, score2 = Game_Checks.checkPointScored(paddle1, paddle2, ball, score1, score2, ballDirX, Window_height, Window_width, LineThickness)
        ballDirX = ballDirX * Game_Checks.checkHitBall(ball, paddle1, paddle2, ballDirX)
        paddle2 = Paddles_New.artificialIntelligence(ball, ballDirX, paddle2)

        Arena.displayScore(screen, score1, score2, WHITE, Font)

        if score1 == 5:
            Game_State.showWinningScreen(screen, clock, FontSize, WHITE, BLACK)
        elif score2 == 5:
            Game_State.showLosingScreen(screen, clock, FontSize, WHITE, BLACK)
        else:
            pygame.display.update()
            clock.tick(FPS)




main()









pygame.quit()
