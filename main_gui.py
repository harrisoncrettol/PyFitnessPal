from email import message
import pygame
import os
from datetime import datetime
from game_funcs import *
from make_account_page import make_account_func
from log_in_page import log_in_func
from dashboard_page import dashboard_func


SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
os.environ['SDL_VIDEO_WINDOW_POS'] = "2000,35"

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyFitnessPal")

pyfit_logo = pygame.image.load("assets//pyfitness_logo.png")

def main_loop():
    create_account = Button(200, 750, 200, 150, "Create Account", size=30, color=DARK_BLUE)
    log_in = Button(600, 750, 200, 150, 'Log In', size=35, color=DARK_BLUE)

    run = True
    while run:
        clock.tick(30)
        screen.fill(BG_COLOR)
        show_img(200, 100, pyfit_logo, screen)

        # check if mouse is over button
        mouse = pygame.mouse.get_pos()
        create_account.draw(screen, mouse)
        log_in.draw(screen, mouse)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_over(create_account, mouse):
                    print("Clicked create account")
                    make_account_func(screen)

                elif is_over(log_in, mouse):
                    print("Clicked log in")
                    user = log_in_func(screen)
                    if user:
                        print("Log in success!")
                        dashboard_func(screen, user)

        pygame.display.update()

    
if __name__ == '__main__':
    main_loop()
    pygame.quit()
    quit()



