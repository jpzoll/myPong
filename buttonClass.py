import pygame
class Button:
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
    def draw(self, win, text, x, y):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])
        font = pygame.font.Font("freesansbold.ttf", 20)
        Text = font.render(text, 1, (0, 0, 0))
        win.blit(Text, (x, y))
    
    def checkIfClicked(self):
        clicked = False
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print("Mouse clicked")
        if mouse_x > self.x and mouse_x < self.x +self.width:
            if mouse_y > self.y and mouse_y < self.y+self.height:
                print("Button clicked")
                clicked = True
                
        return clicked
                
        
            
        
    