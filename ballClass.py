import pygame
import time

pygame.init()

collisionSound = pygame.mixer.Sound("collisionSound.wav")

class Ball:
    def __init__(self, color, x, y, radius, dx, dy, isBouncing):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.isBouncing = isBouncing
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
   
    def move_and_bounce(self, screenWidth, screenHeight, Paddle1, Paddle2):
        self.isBouncing = True
        
        self.x += self.dx
        self.y += self.dy
        
        #Keeps the circle within the bounds of the screen
        #NEVER TRUE AFTER IMPLEMENTING SCORING -- basically useless
            
        if self.x >= (screenWidth - 20) or self.x <= 15:
            self.dx = -self.dx   
        if self.y >= (screenHeight - 20) or self.y <= 20:
            self.dy = -self.dy
            
            
        #Checks for collision with the left paddle/player 1 paddle
        if (Paddle1.x + Paddle1.width) >= (self.x - self.radius) and not (Paddle1.x > self.x):
            if (Paddle1.y <= self.y) and (Paddle1.y + Paddle1.height + 20 >= self.y):
                pygame.mixer.Sound.play(collisionSound)
                self.dx = -self.dx
                #This if statement prevents the bug where the ball gets trapped inside the paddle and the velocity in the x directon (gameBal.dx) is rapidly changing from positive to negative
                if (Paddle1.x + Paddle1.width) >= (self.x - self.radius) and not (Paddle1.x > self.x - self.dx):
                    self.x += self.dx
                
                #Checks for collision with certain portions of left paddle/player 1 paddle
                #middle
                if ((Paddle1.y + 20) <= self.y) and (Paddle1.y + 20 + 25 >= self.y):
                    if self.dy < 0:
                        self.dy += 4
                    elif self.dy > 0:
                        self.dy -= 4
                    self.dx += 2
                    print("Middle portion hit!")
                #top
                elif (Paddle1.y <= self.y) and (Paddle1.y + 20 > self.y):
                    self.dy = -12    #self.dy -= 4
                    print("Top portion hit!")
                #bottom
                elif ((Paddle1.y + 45) <= self.y) and (Paddle1.y + 20 + 25 + 20 >= self.y):
                    self.dy = 12    #self.dy += 4
                    print("Bottom portion hit!")
                else:
                    print("NO SPECIFIC PORTION HIT")
                    
        #Checks for collision with the right paddle/player 2 paddle
        if (Paddle2.x) <= (self.x + self.radius) and not (Paddle2.x < self.x):
            if (Paddle2.y <= self.y) and (Paddle2.y + Paddle2.height + 20 >= self.y):
                pygame.mixer.Sound.play(collisionSound)
                self.dx = -self.dx
                #This if statement prevents the bug where the ball gets trapped inside the paddle and the velocity in the x directon (gameBal.dx) is rapidly changing from positive to negative
                if (Paddle2.x <= self.x + self.radius) and not (Paddle2.x < self.x + self.dx):
                   self.x += self.dx

    def checkSideWallCollision(self, win, screenWidth, player1Score, player2Score):
        #right side
        if (self.x) >= screenWidth - 20:
            player1Score += 1
            scorer = 1
            print("Player 1: " + str(player1Score))
        #left side
        elif (self.x) <= 15:
            player2Score += 1
            scorer = 2
            print("Player 2: " + str(player2Score))
        else:
            scorer = None
        
        return player1Score, player2Score, scorer

    def drawInServingPosition(self, win, scorer, leftPaddle, rightPaddle):
        if scorer == 1:
            self.x = leftPaddle.x + (self.radius + leftPaddle.width)
        elif scorer == 2:
            self.x = rightPaddle.x - (self.radius - rightPaddle.width) - 10
        
        pygame.display.update()
        
    def followPaddle(self, scorer, win, leftPaddle, rightPaddle):
        if scorer == 1:
            self.y = leftPaddle.y + int(leftPaddle.height/2)
        elif scorer == 2:
            self.y = rightPaddle.y + int(rightPaddle.height/2)
            
    def serveBall(self, win, scorer, leftPaddle, rightPaddle):
        gameBall.drawInServingPosition(win, scorer, leftPaddle, rightPaddle)
        gameBall.dx, gameBall.dy = 0, 0
        drawObjects(win, gameBall, leftPaddle, rightPaddle)
        updateScoreboard(win, player1Score, player2Score)
        
        pygame.display.update()
            
        ballInServingPosition = True
        while ballInServingPosition:
            
            if scorer == 1:
                gameBall.followPaddle(1, win, leftPaddle, rightPaddle)
            elif scorer == 2:
                gameBall.followPaddle(2, win, leftPaddle, rightPaddle)
                
            
            pygame.time.delay(30)
            keys = pygame.key.get_pressed()
            win.fill((0, 0, 0))
            gameBall.draw(win)
            leftPaddle.draw(win)
            rightPaddle.draw(win)
            leftPaddle.move(keys, 1)
            rightPaddle.move(keys, 2)
            updateScoreboard(win, player1Score, player2Score)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    ballInServingPosition = False
                    
            pygame.display.update()
                    
        if scorer == 1:
            gameBall.dx, gameBall.dy = 10, -10
        elif scorer == 2:
            gameBall.dx, gameBall.dy = -10, 10
            
        

gameBall = Ball((0, 255, 0), 15, 250, 15, 10, 10, True)