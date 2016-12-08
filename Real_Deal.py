import pygame, sys


FPS = 60



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

def drawArena():
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, ((0,0),(Window_width,Window_height)),LineThickness)

def drawPaddle(paddle):
    if paddle.bottom > Window_height - LineThickness:
        paddle.bottom = Window_height - LineThickness
    elif paddle.top < LineThickness:
        paddle.top = LineThickness

    pygame.draw.rect(screen, WHITE, paddle)

def drawBall(ball):
    pygame.draw.rect(screen, WHITE, ball)

def moveBall(ball,ballDirX,ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LineThickness) or ball.bottom == (Window_height - LineThickness):
        ballDirY = ballDirY * -1
    if ball.left == (LineThickness) or ball.right == (Window_width - LineThickness):
        ballDirX = ballDirX * -1
    return ballDirX, ballDirY

def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else:
        return 1

def checkPointScored(paddle1, paddle2, ball, score1, score2, ballDirX):
    if ball.left == LineThickness:
        score2 += 1
        ball.x = (Window_width/2)
        ball.y = (Window_height/2)
        return score1,score2
    elif ball.right == Window_width - LineThickness:
        score1 += 1
        ball.x = (Window_width/2)
        ball.y = (Window_height/2)
        return score1,score2
    else:
        return score1,score2

def artificialIntelligence(ball, ballDirX, paddle2):
    if ballDirX == -1:
        if paddle2.centery < (Window_height/2):
            paddle2.y += 1
        elif paddle2.centery > (Window_height/2):
            paddle2.y -= 1

    elif ballDirX == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -= 1
    return paddle2

def displayScore(score1, score2):
    p1Score = Font.render('%s' %(score1), True, WHITE)
    p2Score = Font.render('%s' %(score2), True, WHITE)
    screen.blit(p1Score,[75,25])
    screen.blit(p2Score,[225,25])

def main():

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

    
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    
    running = True

    pygame.mouse.set_visible(0)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = event.pos
                paddle1.y = mouseY
                

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        score1, score2 = checkPointScored(paddle1, paddle2, ball, score1, score2, ballDirX)
        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        paddle2 = artificialIntelligence(ball, ballDirX, paddle2)

        displayScore(score1, score2)

        pygame.display.update()
        clock.tick(FPS)

main()









pygame.quit()
