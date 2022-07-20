import pygame
from datetime import datetime
from food_item import read_food_items
from diary_entry import DiaryEntry
from pygame.locals import *
from game_funcs import *
from view_diary_page import view_diary_func
from view_food_database_page import view_food_database_func

def dashboard_func(screen, user):
    # Load/create DiaryEntry obj for today
    today_entry = DiaryEntry()

    # Load food item database
    food_items = read_food_items("databases//food_item_database.txt")

    # Add diary entry if user doesnt have one for today, 
    # else load their entry in today_entry variable
    cur_date = datetime.now().strftime("%Y-%m-%d")
    
    if user.has_entry(cur_date):
        e = user.get_entry(cur_date)
        today_entry.load_data(e, cur_date)

    else:
        user.diary_entries.append(today_entry.to_dict())


    diary_button = Button(100, 800, 300, 150, "Diary", color=DARK_BLUE)
    view_food_button = Button(500, 800, 300, 150, "View Foods", color=DARK_BLUE)
    overview_box = Button(150, 300, 500, 250)

    fork_icon = pygame.image.load("assets//eat.png")
    goal_icon = pygame.image.load("assets//goal.png")

    while True:
        mouse = pygame.mouse.get_pos()

        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                quit()
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if is_over(diary_button, mouse):
                    print("Clicked Diary")
                    view_diary_func(screen, user, today_entry)
                
                elif is_over(view_food_button, mouse):
                    print("Clicked View Food Database")
                    view_food_database_func(screen, user, today_entry, food_items)
                    food_items = read_food_items("databases//food_item_database.txt")
        
        screen.fill(BG_COLOR)
        cals_remaining = int(float(user.calorie_goal) - float(today_entry.get_total_calories()))

        diary_button.draw(screen, mouse)
        view_food_button.draw(screen, mouse)
        overview_box.draw(screen)
        message_display("Welcome back " + str(user.name), 50, 200, 75, screen)
        message_display("Here is today's overview", 40, 200, 200, screen)
        message_display("Calorie Goal:       " + str(user.calorie_goal), 40, 200, 325, screen)
        message_display("Calories Eaten:     " + str(today_entry.get_total_calories()), 40, 200, 400, screen)
        message_display("Calories Remaining: " + str(cals_remaining), 40, 200, 475, screen)

        show_img(155, 330, goal_icon, screen)
        show_img(155, 405, fork_icon, screen)

        pygame.display.update()

