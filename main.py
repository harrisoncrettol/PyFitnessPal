from datetime import datetime
from food_item import create_food_item, read_food_items
from diary_entry import DiaryEntry
from person import User, create_user


# Prints the menu options and returns the user's option
def get_option() -> str:
    print()
    print("1) Create a food item")
    print("2) Show food item database")
    print("3) Show today's diary")
    print("4) Add item to diary")
    print("5) Remove item from diary")
    print("6) Show user data")
    print("7) Create new account")
    print("8) View dashboard")
    option = input("You choose: ")    
    print()
    return option


def main_loop():
    # Load user data
    # if new (default) user, ask them for info
    user = User()
    user.name = "admin"
    user.password = "pass"
    user.calorie_goal = 2000
    user.load_data()

    if user.is_default():
        user = create_user()

    # Load/create DiaryEntry obj for today
    today_entry = DiaryEntry()

    # Load food item database
    food_items = read_food_items("databases//food_item_database.txt")

    # Add diary entry if user doesnt have one for today, 
    # else load their entry in today_entry variable
    cur_date = datetime.now().strftime("%Y-%m-%d")
    
    if user.has_entry(cur_date):
        entry = user.get_entry(cur_date)
        today_entry.load_data(entry, cur_date)

    else:
        user.diary_entries.append(today_entry.to_dict())


    # START MAIN LOOP
    print("Welcome to PyFitnessPal")

    while True:
        option = get_option()
        
        if option == '1': # create food item 
            item = create_food_item()
            item.write("food_item_database.txt")


        elif option == '2': # show food item database
            for item in food_items:
                print(item.description)


        elif option == '3': # show today's entry
            print(today_entry)


        elif option == '4': # add item to diary entry
            today_entry.add_item(food_items)
            user.write_data()


        elif option == '5': # remove item from diary entry
            today_entry.remove_item()
            user.write_data()


        elif option == '6': # show user data
            user.show_data()


        elif option == '7': # create new account/user
            user = create_user()


        elif option == '8': # view dashboard (cals remaining)
            cal_goal, cals_consumed = user.calorie_goal, today_entry.get_total_calories()
            print("Calorie goal: " + str(cal_goal))
            print("Calories consumed: " + str(cals_consumed))
            print("Calories remaining: " + str(float(cal_goal) - float(cals_consumed)))


        else:
            break




if __name__ == '__main__':
    main_loop()




