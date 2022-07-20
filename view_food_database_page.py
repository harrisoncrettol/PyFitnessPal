import pygame
from food_item import FoodItem, write_food_items, read_food_items
from pygame.locals import *
from game_funcs import *
from create_food_item_page import create_food_item_func

def view_food_database_func(screen, user, entry, food_items):

    num_items = len(food_items)

    food_item_box = Button(200, 400, 600, 400, "")
    scroll_left_button = Button(50, 600, 100, 100, "<-")
    scroll_right_button = Button(850, 600, 100, 100, "->")
    add_food_button = Button(200, 200, 150, 150, "Create food", 30)
    remove_food_button = Button(650, 200, 150, 150, "Remove food", 30)

    count = 0
    cur_item = FoodItem()

    while True:
        mouse = pygame.mouse.get_pos()

        for evt in pygame.event.get():
            if evt.type == QUIT:
                return
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if is_over(scroll_left_button, mouse):
                    count -= 1
                if is_over(scroll_right_button, mouse):
                    count += 1

                # CLICKING ADD FOOD BUTTON
                if is_over(add_food_button, mouse):
                    create_food_item_func(screen, food_items)
                    food_items = read_food_items("databases//food_item_database.txt")
                    num_items = len(food_items)

                # CLICKING REMOVE FOOD BUTTON
                if num_items > 0 and is_over(remove_food_button, mouse):
                    i = count%num_items
                    food_items.pop(i)
                    num_items = len(food_items)
                    write_food_items(food_items)

        
        screen.fill(BG_COLOR)
        add_food_button.draw(screen, mouse)

        if num_items > 0:
            food_item_box.draw(screen)
            remove_food_button.draw(screen, mouse)
            scroll_left_button.draw(screen, mouse)
            scroll_right_button.draw(screen, mouse)

            i = count%num_items
            cur_item = food_items[i]
            message_display(str(cur_item), 40, 250, 450, screen)
            message_display("Calories: " + str(cur_item.calories), 40, 250, 500, screen)
            message_display("Protein (g): " + str(cur_item.protein), 40, 250, 550, screen)
            message_display("Carbs (g): " + str(cur_item.carbs), 40, 250, 600, screen)
            message_display("Fat (g): " + str(cur_item.fat), 40, 250, 650, screen)


        pygame.display.update()

