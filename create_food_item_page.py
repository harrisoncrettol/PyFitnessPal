import pygame
import time
from food_item import FoodItem
from pygame.locals import *
from game_funcs import *

def create_food_item_func(screen, items):
    name = ""
    font = pygame.font.Font(None, 50)
    item_added_box = Button(300,400,400,150, "Item added", color=GREEN)
    data = []

    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN and len(data) < 7:
                if evt.unicode.isalpha() or evt.unicode.isdigit() or (evt.unicode == '.') or (evt.unicode == ' '):
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
            message_display("Enter brand name", 50, 325, 400, screen)
        
        elif len(data) == 1:
            message_display("Enter description", 50, 325, 400, screen)

        elif len(data) == 2:
            # check if item exists
            # if it does, then we need to ask other info
            # else, let user know that item does not exist
            for item in items:
                if item.brand_name == data[0].lower() and item.description.lower() == data[1].lower():
                    item_added_box.word = "Item exists"
                    item_added_box.color = RED
                    item_added_box.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    return True

            message_display("Enter serving size", 50, 325, 400, screen)
        
        elif len(data) == 3:
            message_display("Enter calories", 50, 325, 400, screen)

        elif len(data) == 4:
            message_display("Enter protein (g)", 50, 325, 400, screen)
        
        elif len(data) == 5:
            message_display("Enter carbs (g)", 50, 325, 400, screen)
            
        elif len(data) == 6:
            message_display("Enter fat (g)", 50, 325, 400, screen)
            
        else:
            # create FoodItem list with the given data
            data.append(-1) # adds default barcode to data lst
            item = FoodItem()
            item.from_list(data)
            item.write()
            
            item_added_box.draw(screen)
            pygame.display.update()
            time.sleep(1)
            return True
        
        pygame.display.update()
