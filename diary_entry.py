# Each entry will have a list of food items for each meal (breakfast, lunch, diner, snacks)
import json
import copy
from datetime import datetime
from food_item import FoodItem

class DiaryEntry:
    def __init__(self, date=datetime.now().strftime("%Y-%m-%d")):
        self.date = date
        self.meals = {
                        "breakfast": [],
                        "lunch": [],
                        "diner": [],
                        "snacks": [],
        }
    
    # asks user for item name and a meal and adds it to that meal
    # items is food item database (list)
    # returns bool indicating if item was successfully added
    def add_item(self, items) -> bool:
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
            return False

        # ask user for num of servings and to which meal
        user_item.print_item()
        num_servings = float(input("How many servings? (decimal): "))
        which_meal = input("To which meal? (breakfast,lunch,diner,snacks): ")

        # create FoodItem obj with the given data
        lst = user_item.to_list(float(num_servings))

        # add it to the DiaryEntry obj
        self.meals[which_meal].append(lst)
        return True

    def remove_item(self, items) -> bool:
        # ask user for item to remove and to which meal
        food_name = input("Type in a food to remove: ")
        which_meal = input("To which meal? (breakfast,lunch,diner,snacks): ")
        
        # make sure item exists
        for item in self.meals[which_meal]:
            if item[0].lower() == food_name.lower():
                self.meals[which_meal].remove(item)
                print("Item was removed.")
                return True
        
        print("Item not found")
        return False


    # returns total calories for the given entry
    def get_total_calories(self) -> float:
        total = 0
        cur_item = FoodItem()
        for key in self.meals.keys():
            if self.meals[key]:
                for lst in self.meals[key]:
                    cur_item.lst_to_item(lst)
                    total += cur_item.calories
        
        return total


    def print_entry(self):
        cur_item = FoodItem()
        meal_items = []
        for key in self.meals.keys():
            if self.meals[key]:
                for lst in self.meals[key]:
                    cur_item.lst_to_item(lst)
                    meal_items.append(str(cur_item))
            print("{}: {}".format(key, meal_items))
            meal_items.clear()

    

    def to_json(self):
        return json.dumps(self.to_dict())

    # returns a dictionary with DiaryEntry data
    def to_dict(self):
        return {self.date: self.meals}

    # d is dict
    # date is key for dict
    def load_data(self, d, date):
        self.date = date
        self.meals = d[date]

