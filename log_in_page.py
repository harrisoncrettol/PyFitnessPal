import pygame
import os
import time
from person import User
from pygame.locals import *
from game_funcs import *

def log_in_func(screen):
    name = ""
    font = pygame.font.Font(None, 50)
    verified = Button(300, 400, 400, 150, "Login successful", color=GREEN)
    invalid = Button(300, 350, 500, 150, "Invalid name or password", color=RED)
    data = []
    run = True
    while run:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN and len(data) < 2:
                if evt.unicode.isalpha() or evt.unicode.isdigit():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    data.append(name)
                    name = ""
            elif evt.type == QUIT:
                return
        screen.fill(DARK_BLUE)
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        
        if len(data) == 0:
            message_display("Type Username", 50, 325, 400, screen)
        
        elif len(data) == 1:
            message_display("Type Password", 50, 325, 400, screen)

        else:
            for f in os.listdir('users'):
                if f == "{}_{}.txt".format(data[0], data[1]):
                    verified.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    usr = User(data[0], data[1])
                    usr.load_data()
                    return usr

            else:
                invalid.draw(screen)
                pygame.display.update()
                time.sleep(1)
                return None

        pygame.display.update()