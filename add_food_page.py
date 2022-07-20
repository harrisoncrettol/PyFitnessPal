import pygame
import time
import copy
from food_item import read_food_items
from pygame.locals import *
from game_funcs import *

def add_food_func(screen, meal, entry):
    items = read_food_items("databases//food_item_database.txt")
    name = ""
    font = pygame.font.Font(None, 50)
    item_added_box = Button(300,400,400,150, "Item added", color=GREEN)
    data = []

    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN and len(data) < 3:
                if evt.unicode.isalpha() or evt.unicode.isdigit() or (evt.unicode == '.'):
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
            message_display("Enter food", 50, 325, 400, screen)
        elif len(data) == 1:
            # check if item exists
            # if it does, then we need to show nutrition and ask how many servings
            # else, let user know that item does not exist
            found_item = None
            for item in items:
                if item.description.lower() == data[0].lower():
                    found_item = copy.deepcopy(item)
            
            if found_item is None:
                item_added_box.color = RED
                item_added_box.word = "Item not found"
                item_added_box.draw(screen)
                pygame.display.update()
                time.sleep(1)
                return False

            
            message_display("How many servings? (decimal)", 45, 250, 300, screen)
            message_display(str(found_item), 40, 250, 600, screen)
            message_display("Calories: " + str(found_item.calories), 40, 250, 650, screen)
            message_display("Protein (g): " + str(found_item.protein), 40, 250, 700, screen)
            message_display("Carbs (g): " + str(found_item.carbs), 40, 250, 750, screen)
            message_display("Fat (g): " + str(found_item.fat), 40, 250, 800, screen)
            

        else:
            # create FoodItem list with the given data
            lst = found_item.to_list(float(data[1]))

            # add it to the DiaryEntry obj
            entry.meals[meal].append(lst)

            item_added_box.draw(screen)
            pygame.display.update()
            time.sleep(1)
            return True
        
        pygame.display.update()
