import pygame
import os
import time
import json
from person import User
from pygame.locals import *
from game_funcs import *

def make_account_func(screen):
    name = ""
    font = pygame.font.Font(None, 50)
    created_box = Button(300,400,400,150, "Account Created", color=GREEN)
    data = []

    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN and len(data) < 3:
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
        elif len(data) == 2:
            message_display("Enter Calorie Goal", 45, 325, 400, screen)

        else:
            created_box.draw(screen)
            # creates user txt file
            n, p, c = data
            usr = User(n,p,c)
            usr.show_data()
            usr.write_data()
            pygame.display.update()
            time.sleep(1)
            break
        
        pygame.display.update()
