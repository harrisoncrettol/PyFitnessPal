import pygame
import os
import time
import json
from datetime import datetime
from food_item import FoodItem, read_food_items, create_food_item
from diary_entry import DiaryEntry
from person import User
from pygame.locals import *
from game_funcs import *
from add_food_page import add_food_func

def view_meal_func(screen, user, entry, meal):

    # Need to figure out how many items are in the meal
    meal_items = entry.meals[meal]
    num_items = len(meal_items)

    food_item_box = Button(200, 400, 600, 400, "")
    scroll_left_button = Button(50, 600, 100, 100, "<-")
    scroll_right_button = Button(850, 600, 100, 100, "->")
    add_food_button = Button(200, 200, 150, 150, "Add food", 30)
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
                    add_success = add_food_func(screen, meal, entry)
                    if add_success:
                        meal_items = entry.meals[meal]
                        num_items = len(meal_items)
                        user.write_data()

                # CLICKING REMOVE FOOD BUTTON
                if num_items > 0 and is_over(remove_food_button, mouse):
                    i = count%num_items
                    meal_items.pop(i)
                    num_items = len(meal_items)
                    user.write_data()


        
        screen.fill(BG_COLOR)
        message_display(str(meal), 65, 400, 75, screen)
        add_food_button.draw(screen, mouse)


        if num_items > 0:
            food_item_box.draw(screen)
            remove_food_button.draw(screen, mouse)
            scroll_left_button.draw(screen, mouse)
            scroll_right_button.draw(screen, mouse)

            i = count%num_items
            cur_item.from_list(meal_items[i])
            message_display(str(cur_item), 40, 250, 450, screen)
            message_display("Calories: " + str(cur_item.calories), 40, 250, 500, screen)
            message_display("Protein (g): " + str(cur_item.protein), 40, 250, 550, screen)
            message_display("Carbs (g): " + str(cur_item.carbs), 40, 250, 600, screen)
            message_display("Fat (g): " + str(cur_item.fat), 40, 250, 650, screen)


        pygame.display.update()

