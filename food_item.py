
#description,brand_name,serving_size,calories,carbs(g),fat(g),protein(g),sodium(mg),sugar(g),fiber(g)

class FoodItem:
    def __init__(self, description="", brand_name="", serving_size="", calories=0, carbs=0, fat=0, protein=0, sodium=0, fiber=0):
        self.description = description
        self.brand_name = brand_name
        self.serving_size = serving_size
        self.calories = calories
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        self.sodium = sodium
        self.fiber = fiber

    def __str__(self):
        return "{} {}".format(str(self.serving_size), str(self.description))

    def lst_to_item(self, lst):
        self.description = lst[0]
        self.brand_name = lst[1]
        self.serving_size = lst[2]
        self.calories = lst[3]
        self.carbs = lst[4]
        self.fat = lst[5]
        self.protein = lst[6]
        self.sodium = lst[7]
        self.fiber = lst[8]

    def to_list(self, scale=1.0) -> list: # scale: scales the nutrition facts
        scaled_serving_size = "{} {}".format(float(self.serving_size.split()[0])*scale, " ".join(self.serving_size.split()[1:]))
        return [self.description, self.brand_name, scaled_serving_size, float(self.calories)*scale, float(self.carbs)*scale, float(self.fat)*scale, float(self.protein)*scale, float(self.sodium)*scale, float(self.fiber)*scale]

    def print_item(self):
        print("Description: " + str(self.description))
        print("Brand Name: " + str(self.brand_name))
        print("Serving Size: " + str(self.serving_size))
        print("Calories: " + str(self.calories))
        print("Carbs: " + str(self.carbs))
        print("Fat: " + str(self.fat))
        print("Protein: " + str(self.protein))
        print("Sodium: " + str(self.sodium))
        print("Fiber: " + str(self.fiber))
        print()

    def print_small(self): # prints essiential details
        print("Description: " + str(self.description))
        print("Serving Size: " + str(self.serving_size))
        print("Calories: " + str(self.calories))
        print("Fat: " + str(self.fat))
        print("Protein: " + str(self.protein))
        print()



# reading food items from file into a list and returns list
def read_items() -> list:
    f = open("food_nutrition_value.txt", "r")
    items = []
    for i,line in enumerate(f.read().split("\n")):
        cur_item = FoodItem()
        cur_item.lst_to_item(line.split(","))
        items.append(cur_item)
    return items


# writes food items to file
def write_item(item:FoodItem) -> None:
    f = open("food_nutrition_value.txt", "a")
    
    line = ",".join([str(i) for i in item.to_list()])
    f.write("\n")
    f.write(line)
    
    f.close()
    
    


# create_food: creates and returns a food item based on the parameters
def create_food() -> FoodItem:
    item = FoodItem()
    item.brand_name = input("Brand Name: ")
    item.description = input("Description: ")
    item.serving_size = input("Serving Size: ")
    item.calories = input("Calories: ")
    item.carbs = input("Carbs (g): ")
    item.fat = input("Fat (g): ")
    item.protein = input("Protein (g):")
    item.fiber = input("Fiber (g): ")
    item.sodium = input("Sodium (mg): ")
    return item



# NEED A FUNCTION THAT TAKES IN A LIST CONTAINING FOOD ITEM DATA
# AND MAKES A FOOD ITEM OBJECT OUT OF IT