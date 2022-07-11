# Each entry will have a list of food items for each meal (breakfast, lunch, diner, snacks)
import json
from datetime import datetime

class DiaryEntry:
    def __init__(self, date=datetime.now().strftime("%Y-%m-%d")):
        self.date = date
        self.meals = {
                        "breakfast": [],
                        "lunch": [],
                        "diner": [],
                        "snacks": [],
        }
    

    def print_entry(self):
        for key in self.meals.keys():
            print("{}: {}".format(key, self.meals[key]))
    

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

