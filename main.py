# User class:     - list of days logged, calorie goal, weight goal, height, weight
# FoodItem class: - 
import copy
import json
from datetime import datetime
from food_item import FoodItem, read_items, write_items
from diary_entry import DiaryEntry
from user import UserData

def print_menu():
    print()
    print("1) View Dashboard") # Shows calorie base goal and calories remaining
    print("2) View Today's Diary")
    print("3) Add Item to Diary")
    print("4) Show Food Database")
    print("5) Show user data")


def main_loop():
    with open("user_data.txt", "r") as f:
        data = f.read()
     
    admin = UserData()
    admin.load_data(data)
    

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
            pass


        elif menu_option == "2": # view today's diary entry
            today_entry.print_entry()


        elif menu_option == "3": # add item to diary
            # ask user for an item
            food_name = input("Type in food: ")
            # make sure item exists
            food_found = False
            user_item = None
            
            for item in items:
                if item.description.lower() == food_name.lower():
                    food_found = True
                    user_item = copy.deepcopy(item)
                    break
            
            if not food_found:
                print("Item not found")
                continue

            # ask user for num of servings and to which meal
            user_item.print_item()
            num_servings = float(input("How many servings? (decimal): "))
            which_meal = input("To which meal? (breakfast,lunch,diner,snacks): ")

            # create FoodItem obj with the given data
            lst = user_item.to_list(float(num_servings))
            # print scaled user item
            #print(lst)

            # add it to today's DiaryEntry obj
            today_entry.meals[which_meal].append(lst)
            admin.write_data()

    
        elif menu_option == "4": # show food database
            for item in items:
                item.print_description()
        

        elif menu_option == "5": # print user data
            admin.print_data()

        
        else:
            print("Invalid option")
            continue


main_loop()