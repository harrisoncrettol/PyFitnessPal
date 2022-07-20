# Food items have: brand name, description, serving size, 
#                  calories, protein (g), carbs (g), fat (g)

class FoodItem:
    def __init__(self, brand_name="", description="", serving_size="", cals=0, protein=0, carbs=0, fat=0):
        self.brand_name = brand_name
        self.description = description
        self.serving_size = serving_size
        self.calories = cals
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def __str__(self) -> str:
        return "{} {}".format(self.serving_size, self.description)


    def print_item(self) -> None:
        print("Description: {} {}\nCalories: {}".format(self.serving_size, self.description, self.calories))

    # returns list version of object
    def to_list(self, scale=1.0) -> list:
        num, amt = self.serving_size.split()
        new_servings = "{} {}".format(str(float(num)*scale), amt)
        return [self.brand_name, self.description, new_servings, float(self.calories)*scale, float(self.protein)*scale, float(self.carbs)*scale, float(self.fat)*scale]

    def from_list(self, lst) -> None:
        self.brand_name = lst[0]
        self.description = lst[1]
        self.serving_size = lst[2]
        self.calories = lst[3]
        self.protein = lst[4]
        self.carbs = lst[5]
        self.fat = lst[6]

    def write(self, filename="databases//food_item_database.txt") -> None:
        line = ",".join([str(i) for i in self.to_list()]) + '\n'
        with open(filename, "a") as f:
            f.write(line)



# prompts user for item info and returns that food item obj
def create_food_item() -> FoodItem:
    brand = input("Enter brand name: ")
    description = input("Enter description: ")
    serving_size = input("Enter serving size: ")
    cals = input("Enter calories: ")
    protein = input("Enter protein (g): ")
    carbs = input("Enter carbohydrates (g): ")
    fat = input("Enter fat (g): ")
    return FoodItem(brand, description, serving_size, cals, protein, carbs, fat)


# returns list of lists containing food item data
def read_food_items(filename) -> list:
    items = []
    with open(filename, "r") as f:
        for line in f.read().split("\n")[:-1]:
            item = FoodItem()
            item.from_list(line.split(","))
            items.append(item)
    
    return items

def write_food_items(items, filename="databases//food_item_database.txt"):
    with open(filename, "w") as f:
        for item in items:
            item.write(filename)

