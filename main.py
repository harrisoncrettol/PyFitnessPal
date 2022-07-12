# User class:     - list of days logged, calorie goal, weight goal, height, weight
# FoodItem class: - 
import copy
import json
from datetime import datetime
from food_item import FoodItem, read_items, write_item, create_food
from diary_entry import DiaryEntry
from user import UserData

def print_menu():
    print()
    print("1) View Dashboard") # Shows calorie base goal and calories remaining
    print("2) View Today's Diary")
    print("3) Add Item to Diary")
    print("4) Remove Item from Diary")
    print("5) Show Food Item Database")
    print("6) Add Food Item to Database")


def main_loop():
    with open("user_data.txt", "r") as f:
        data = f.read()
     
    admin = UserData()
    admin.load_data(data)
    
    # make sure user has data (if not we need to prompt them for all their info)


    items = read_items()
    today_entry = DiaryEntry()
    
    # add diary entry if user doesn't have one for today. else load their diary entry into an obj
    cur_date = datetime.now().strftime("%Y-%m-%d")

    if admin.has_entry(cur_date):
        entry = admin.get_entry(cur_date)
        today_entry.load_data(entry, cur_date)

    else:
        admin.diary_entries.append(today_entry.to_dict())



    # START MAIN LOOP
    print("Hello welcome to PyFitnessPal")

    while True:
        print_menu()
        menu_option = input("Your choice (-1 to quit): ")
        if menu_option == "-1": # quit
            break


        elif menu_option == "1": # view dashboard (cal goal and cal renmaining)
            daily_total = today_entry.get_total_calories()
            cals_left = admin.calorie_goal - daily_total
            print("Calorie goal is: " + str(int(admin.calorie_goal)))
            print("Calories eaten today: " + str(int(daily_total)))
            print("Calories remaining: " + str(int(cals_left)))


        elif menu_option == "2": # view today's diary entry
            today_entry.print_entry()


        elif menu_option == "3": # add item to diary
            today_entry.add_item(items)
            admin.write_data()

    
        elif menu_option == "4": # remove item from diary
            today_entry.remove_item(items)

        

        elif menu_option == "5": # print food item database
            for item in items:
                item.print_small()


        elif menu_option == "6":
            item = create_food()
            write_item(item)
            items = read_items()

        
        else:
            print("Invalid option")
            continue


main_loop()