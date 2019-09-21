import pygame, sys
pygame.init()

def pause(win):
    print("Game is Paused")
    paused = True
    keys = pygame.key.get_pressed()
    
    while paused:
        myFont = pygame.font.SysFont("monospace", 45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = False
                    print("Game is unpaused")
        win.fill((255, 255, 255))
        pauseText = myFont.render("Paused", 1, (0, 0, 0))
        win.blit(pauseText, (165, 200))
        pygame.display.update()
        
    
def main():
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Making a ball bounce")

    screenWidth = 500 - 15
    x = 15
    y = 250
    dx = 10
    direction = "right"

    run = True
    while run:
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause(win)

        keys = pygame.key.get_pressed()
        
                
        pygame.draw.circle(win, (0, 255, 0), (x, y), 15)
        pygame.display.update()       

        isBouncing = True
            
            
        while isBouncing:
            if direction == "right":
                x += dx
                if x >= screenWidth:
                    direction = "left"
            elif direction == "left":
                x -= dx
                if x >= screenWidth or x <= 15:
                    direction = "right"
            pygame.display.update()
            isBouncing = False
                
        
            
        win.fill((0, 0, 0))

main()    

pygame.quit()
