import pygame

class Paddle:
    def __init__(self, color, x, y, dx, dy, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.height = height
        self.width = width
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])
        
    def move(self, keys, player):
        if player == 1:
            if keys[pygame.K_w] and self.y >= 0:
                self.y -= self.dy
            if keys[pygame.K_s] and self.y <= 485:
                self.y += self.dy
        elif player == 2:
            if keys[pygame.K_UP] and self.y >= 0:
                self.y -= self.dy
            if keys[pygame.K_DOWN] and self.y <= 485:
                self.y += self.dy
                    
    def CPU_move(self, ball, scorer):
        
        if (ball.y < self.y) and (ball.y > self.y + self.height):
            self.dy = 0
            self.y += self.dy
        if (self.x - ball.x) > 350:
            self.dy = 0
            self.y += self.dy
        else:
            if ball.y < self.y + self.height:
                self.dy = 12
                self.y -= self.dy
            if ball.y > self.y and not (ball.dy < 0):
                self.dy = 12
                self.y += self.dy 
            
        
        
        
        

#leftPaddle = Paddle((255, 255, 255), 40, 150, 0, 10, 10, 65)
#rightPaddle = Paddle((255, 255, 255), 460, 150, 0, 10, 10, 65)