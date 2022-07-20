import pygame
from datetime import date, timedelta
from diary_entry import DiaryEntry
from pygame.locals import *
from game_funcs import *
from view_meal_page import view_meal_func


def view_diary_func(screen, user, entry):
    breakfast_cals = str(entry.get_total_meal("breakfast"))
    lunch_cals = str(entry.get_total_meal("lunch"))
    dinner_cals = str(entry.get_total_meal("dinner"))
    snacks_cals = str(entry.get_total_meal("snacks"))
    
    breakfast_button = Button(200, 600, 500, 75, "Breakfast: " + breakfast_cals + " calories")
    lunch_button = Button(200, 700, 500, 75, "Lunch: " + lunch_cals + " calories")
    dinner_button = Button(200, 800, 500, 75, "Dinner: " + dinner_cals + " calories")
    snacks_button = Button(200, 900, 500, 75, "Snacks: " + snacks_cals + " calories")
    overview_box = Button(200, 250, 500, 250)

    prev_date_button = Button(300, 50, 50, 50, "<-", 30)
    next_date_button = Button(700, 50, 50, 50, "->", 30)


    while True:
        mouse = pygame.mouse.get_pos()

        for evt in pygame.event.get():
            if evt.type == QUIT:
                return
            if evt.type == pygame.MOUSEBUTTONDOWN:
                # CLICKING BREAKFAST BUTTON
                if is_over(breakfast_button, mouse):
                    view_meal_func(screen, user, entry, "breakfast")
                # CLICKING LUNCH BUTTON
                elif is_over(lunch_button, mouse):
                    view_meal_func(screen, user, entry, "lunch")
                # CLICKING DINNER BUTTON
                elif is_over(dinner_button, mouse):
                    view_meal_func(screen, user, entry, "dinner")
                # CLICKING SNACKS BUTTON
                elif is_over(snacks_button, mouse):
                    view_meal_func(screen, user, entry, "snacks")

                # CLICKING PREVIOUS DAY BUTTON
                elif is_over(prev_date_button, mouse):
                    # need to retreive diary entry from previous day
                    # or create one if it doesn't exist
                    td = timedelta(days=1)
                    cur_entry_date = date.fromisoformat(entry.date)
                    prev_date = str(cur_entry_date - td)
                    
                    if user.has_entry(prev_date):
                        d = user.get_entry(prev_date)
                        entry = DiaryEntry()
                        entry.load_data(d, prev_date)
                    else:
                        entry = DiaryEntry(prev_date)
                        user.diary_entries.append(entry.to_dict())
                        user.write_data()
                # CLICKING NEXT DAY BUTTON
                elif is_over(next_date_button, mouse):
                    td = timedelta(days=1)
                    cur_entry_date = date.fromisoformat(entry.date)
                    next_date = str(cur_entry_date + td)

                    if user.has_entry(next_date):
                        d = user.get_entry(next_date)
                        entry = DiaryEntry()
                        entry.load_data(d, next_date)
                    else:
                        entry = DiaryEntry(next_date)
                        user.diary_entries.append(entry.to_dict())
                        user.write_data()
                    

        
        breakfast_cals = str(entry.get_total_meal("breakfast"))
        lunch_cals = str(entry.get_total_meal("lunch"))
        dinner_cals = str(entry.get_total_meal("dinner"))
        snacks_cals = str(entry.get_total_meal("snacks"))
        
        total_cals, total_protein, total_carbs, total_fat = [str(i) for i in entry.get_totals()]
        
        breakfast_button.word = "Breakfast: " + breakfast_cals + " calories"
        lunch_button.word = "Lunch: " + lunch_cals + " calories"
        dinner_button.word = "Dinner: " + dinner_cals + " calories"
        snacks_button.word = "Snacks: " + snacks_cals + " calories"

        screen.fill(BG_COLOR)
        overview_box.draw(screen)
        message_display("Date: " + str(entry.date), 40, 400, 50, screen)

        message_display("Total cals:        " + total_cals, 35, 200, 255, screen)
        message_display("Total protein (g): " + total_protein, 35, 200, 305, screen)
        message_display("Total carbs (g):   " + total_carbs, 35, 200, 355, screen)
        message_display("Total fat (g):     " + total_fat, 35, 200, 405, screen)

        
        prev_date_button.draw(screen, mouse)
        next_date_button.draw(screen, mouse)
        breakfast_button.draw(screen, mouse)
        lunch_button.draw(screen, mouse)
        dinner_button.draw(screen, mouse)
        snacks_button.draw(screen, mouse)

        pygame.display.update()

