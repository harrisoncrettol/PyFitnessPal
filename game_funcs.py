import pygame

RED = (255,0,0)
GREEN = (50,220,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_BLUE = (0,102,238)
DARK_BLUE = (0, 84, 139)
BG_COLOR = (40,40,40)

pygame.init()

def show_img(x, y, picture, screen):
    screen.blit(picture, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def message_display(text, size, x, y, screen):
    largeText = pygame.font.SysFont('helvetica', size)
    textSurf, textRect = text_objects(text, largeText)
    textRect = (x, y)
    screen.blit(textSurf, textRect)

def is_over(arg, mouse):
    if arg.x < mouse[0] < arg.x + arg.w and arg.y < mouse[1] < arg.y + arg.h:
        return True

class Button():
    def __init__(self, x, y, w, h, word='', size=40, color=LIGHT_BLUE):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.word = word
        self.size = size
        self.color = color

    def set_word(self, word):
        self.word = word

    #this function makes it so you dont have to "pygame.draw.rect" when drawing to the screen
    def draw(self, screen, mouse=None):
        # if the mouse is over the button: draw rect with lighter color
        # else: draw rect with darker color
        if mouse is None:
            pygame.draw.rect(screen, tuple([i-50 if i-50>0 else 0 for i in self.color]), (self.x, self.y, self.w, self.h))

        elif is_over(self, mouse):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(screen, tuple([i-50 if i-50>0 else 0 for i in self.color]), (self.x, self.y, self.w, self.h))
        
        message_display(self.word, self.size, self.x, self.y, screen)

