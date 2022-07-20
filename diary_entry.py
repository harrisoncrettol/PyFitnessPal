from datetime import datetime
from food_item import FoodItem
import copy

class DiaryEntry:
    def __init__(self, date=datetime.now().strftime("%Y-%m-%d")):
        self.date = date
        self.meals = {
                        "breakfast": [],
                        "lunch": [],
                        "dinner": [],
                        "snacks": []
        }

    def __str__(self):
        s = "Date: {}\n".format(self.date)
        cur_item = FoodItem()
        meal_items = []

        for key in self.meals.keys():
            if self.meals[key]:
                for lst in self.meals[key]:
                    cur_item.from_list(lst)
                    meal_items.append(str(cur_item))
            s += "{}: {}\n".format(key, meal_items)
            meal_items.clear()
        return s

    
    # add_item: asks user for item name and a meal and adds it to that meal
    # items is food item database (list)
    # returns bool indicating if item was added successfully
    def add_item(self, items) -> bool:
        # ask user for item name
        food_name = input("Enter a food name: ")

        # if item is in food database, print it, else return False
        found_item = None
        for item in items:
            if item.description.lower() == food_name.lower():
                found_item = copy.deepcopy(item)
        
        if found_item is None:
            print("Item not found.")
            return False

        # prompt for num servings and to which meal
        num_servings = input("How many servings (decimal): ")
        which_meal = input("Which meal (breakfast, lunch, dinner, snacks): ").lower()
        
        # create FoodItem list with the given data
        lst = found_item.to_list(float(num_servings))

        # add it to the DiaryEntry obj
        self.meals[which_meal].append(lst)

    # remove_item: removes item from specified meal
    # returns bool indicating if item was added successfully
    def remove_item(self) -> bool:
        food_name = input("Type in a food to remove: ")
        which_meal = input("To which meal? (breakfast,lunch,dinner,snacks): ")

        for item in self.meals[which_meal]:
            if item[1].lower() == food_name.lower():
                self.meals[which_meal].remove(item)
                print("Item was removed.")
                return True
        print("Item not found")
        return False

    # calculates and returns total calories consumed
    def get_total_calories(self) -> float:
        total = 0
        cur_item = FoodItem()
        for key in self.meals.keys():
            if self.meals[key]:
                for lst in self.meals[key]:
                    cur_item.from_list(lst)
                    total += float(cur_item.calories)
        return total

    # calculates and returns total macros in this form: [cals, protein, carb, fat]
    def get_totals(self) -> list:
        totals = [0,0,0,0]
        cur_item = FoodItem()
        for key in self.meals.keys():
            if self.meals[key]:
                for lst in self.meals[key]:
                    cur_item.from_list(lst)
                    totals[0] += float(cur_item.calories)
                    totals[1] += float(cur_item.protein)
                    totals[2] += float(cur_item.carbs)
                    totals[3] += float(cur_item.fat)
        return totals

    def get_total_meal(self, meal) -> float:
        total = 0
        cur_item = FoodItem()
        for lst in self.meals[meal]:
            cur_item.from_list(lst)
            total += cur_item.calories
        return total

    

    # returns dictionary version of obj
    def to_dict(self) -> dict:
        return {self.date: self.meals}

    # d is dictionary version of a DiaryEntry obj
    # date is the date of the entry
    def load_data(self, d, date) -> None:
        self.date = date
        self.meals = d[date]

