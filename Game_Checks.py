import pygame,sys,random

pygame.init()

def checkEdgeCollision(ball, ballDirX, ballDirY, Window_height, Window_width, LineThickness):
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

def checkPointScored(paddle1, paddle2, ball, score1, score2, ballDirX, Window_height, Window_width, LineThickness):
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
