import pygame, sys
import time
from buttonClass import Button
from ballClass import Ball
from paddleClass import Paddle
pygame.init()


def updatePaddles(win, keys):
    leftPaddle.draw(win)
    rightPaddle.draw(win)

    leftPaddle.move(keys, 1)
    rightPaddle.move(keys, 2)

def drawObjects(win, gameBall, leftPaddle, rightPaddle):
    
    win.fill((0, 0, 0))
    
    gameBall.draw(win)
    leftPaddle.draw(win)
    rightPaddle.draw(win)
    leftPaddle.move(keys, 1)
    rightPaddle.move(keys, 2)
    
    pygame.display.update()
    

def getItemCenterCoords(Item):
    itemCenter_x = 500/2 - Item.get_rect().width/2
    itemCenter_y = 550/2 - Item.get_rect().height/2
    
    return itemCenter_x, itemCenter_y

def gameOverScreen(win, winner):
    gameOverScreen = True
    while gameOverScreen:
        pygame.display.flip()
        win.fill((255, 255, 255))
        
        gameOverFont = pygame.font.SysFont("Arial", 50)
        gameOverText = gameOverFont.render("Game Over!", 1, (0, 0, 0))
        
        winnerFont = pygame.font.SysFont("Arial", 30)
        winnerText = winnerFont.render("Player " + str(winner) + " has won", 1, (0, 0, 0))
        
        gameOverText_x, gameOverText_y = getItemCenterCoords(gameOverText)
        winnerText_x, winnerText_y = getItemCenterCoords(winnerText)
        win.blit(gameOverText, (gameOverText_x, gameOverText_y))
        win.blit(winnerText, (winnerText_x, winnerText_y + 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main()

def updateScoreboard(win, player1Score, player2Score):
    player1Font = pygame.font.SysFont("Arial", 30)
    player1Text = player1Font.render(str(player1Score), 1, (255, 255, 255))
    
    player2Font = pygame.font.SysFont("Arial", 30)
    player2Text = player2Font.render(str(player2Score), 1, (255, 255, 255))
    
    win.blit(player1Text, (150, 50))
    win.blit(player2Text, (300, 50))
    
def displayScoringPlay(win, scorer, gameBall, leftPaddle, rightPaddle):
    if not (scorer == None):
        
        scorePlayFont = pygame.font.SysFont("Arial", 30)
        scorePlayText = scorePlayFont.render("Player " + str(scorer) + " scores!", 1, (255, 255, 255))
        
        x, y = getItemCenterCoords(scorePlayText)
        win.blit(scorePlayText, (x, 400))
        pygame.display.update()
        
        scorePlayTextDisplayed = True
        while scorePlayTextDisplayed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    scorePlayTextDisplayed = False
        
        
        pygame.display.update()
            
        serveBall(win, scorer)
        
        #time.sleep(2)
                
        drawObjects(win, gameBall, leftPaddle, rightPaddle)
        
def serveBall(win, scorer):
    
    gameBall.drawInServingPosition(win, scorer, leftPaddle, rightPaddle)
    gameBall.dx, gameBall.dy = 0, 0
    drawObjects(win, gameBall, leftPaddle, rightPaddle)
    updateScoreboard(win, player1Score, player2Score)
    
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
        


def checkGameOver(player1Score, player2Score):
    if player1Score == 5 or player2Score == 5:
        if player1Score == 5:
            winner = 1
        elif player2Score == 5:
            winner = 2
        return winner

def pause(win):
    print("Game is Paused")
    paused = True
    keys = pygame.key.get_pressed()
    
    while paused:
        myFont = pygame.font.SysFont("monospace", 45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = False
                    print("Game is unpaused")
        win.fill((255, 255, 255))
        pauseText = myFont.render("Paused", 1, (0, 0, 0))
        textCenter_x = 500/2 - pauseText.get_rect().width/2
        textCenter_y = 550/2 - pauseText.get_rect().height/2
        win.blit(pauseText, (textCenter_x, textCenter_y))
        pygame.display.update()
   
#Displays the start menu
def startMenu(win):
    startMenu = True
    while startMenu:
        pygame.time.delay(25)
        #Creates the start button from the button class
        startButton = Button((255, 255, 0), 200, 300, 100, 50)
        startButton.draw(win, "Start", screenWidth / 2, (screenHeight / 2) + 50)
        pygame.display.update()
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                startMenu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checks if the  button was clicked by invoking the button class method 'checkIfClicked'
                if startButton.checkIfClicked() == True:
                    startMenu = False
          
        #Draws the text on the button
        win.fill((255, 255, 255))    
        titleText = pygame.font.SysFont("arialblack", 25)
        titleText = titleText.render("Welcome to Pong!", 1, (0, 0, 0))
        win.blit(titleText, (125, 150))
        
    win.fill((255, 255, 255))
    pygame.display.update()

###################################################################
            
###################################################################
            
###################################################################
            
###################################################################
            
###################################################################


def main():
    global screenHeight
    global screenWidth
    screenWidth, screenHeight = 500, 550
    win = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Pong - Joe Zoll")
    #Start Menu is displayed until user takes action to proceed to the actual game
    startMenu(win)
    
    #Initialize the game ball and the paddles
    global gameBall
    global leftPaddle
    global rightPaddle
    gameBall = Ball((0, 255, 0), 490, 250, 15, 10, -10, True)
    leftPaddle = Paddle((255, 255, 255), 40, 160, 0, 15, 10, 65)
    rightPaddle = Paddle((255, 255, 255), 460 - 10, 210, 0, 15, 10, 65)
        
    global player1Score
    global player2Score
    player1Score = 0
    player2Score = 0
    
    isFirstServe = True
    
    running = True
    while running:
        #Determines the frame rate
        pygame.time.delay(30)
        #Takes in list of bools for each key;
            #True if pressed, False if not
        global keys
        keys = pygame.key.get_pressed()
        
        #Event handler loop for quitting and pausing the game
        for event in pygame.event.get():
            if (event.type == pygame.QUIT
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause(win)

        #Draws the circle and the paddle(s) in the current x and y position they're in
        win.fill((0, 0, 0))
        gameBall.draw(win)
        leftPaddle.draw(win)
        rightPaddle.draw(win)
        gameBall.move_and_bounce(screenWidth, screenHeight, leftPaddle, rightPaddle)
        leftPaddle.move(keys, 1)
        rightPaddle.move(keys, 2)
        updateScoreboard(win, player1Score, player2Score)
        
        #Updates the screen to show the circle and paddle(s)
        pygame.display.update()
        
        if isFirstServe:
            serveBall(win, 1)
            isFirstServe = False
        
        #Increments/decrements the x and y, basically how the circle moves
        player1Score, player2Score, scorer = gameBall.checkSideWallCollision(win, screenWidth, player1Score, player2Score)
        displayScoringPlay(win, scorer, gameBall, leftPaddle, rightPaddle)
        pygame.display.update()
        #win.fill((0, 0, 0))
        
        winner = checkGameOver(player1Score, player2Score)
        if not (winner == None):
            running = False
       
    gameOverScreen(win, winner)
    print("Player " + str(winner) + " wins!")

main()    


main()