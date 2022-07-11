# list of diary entries for each day logged
# calories remaining
import json
from datetime import datetime

class UserData:
    def __init__(self,name=""):
        self.name = name
        self.calorie_goal = 0
        self.diary_entries = []

    # returns bool indicating if entry exists for that day 
    def has_entry(self, date) -> None:
        for entry in self.diary_entries:
            if date in entry.keys():
                return True
        return False

    # Precondition: there must be an entry for the supplied date
    def get_entry(self, date) -> dict:
        for entry in self.diary_entries:
            if date in entry.keys():
                return entry

    def to_dict(self):
        return {"name": self.name, "calorie_goal": self.calorie_goal, "diary_entries": self.diary_entries }

    def write_data(self):
        with open("user_data.txt", "w") as f:
            f.write(json.dumps(self.to_dict()))

    def load_data(self, json_str):
        d = json.loads(json_str)
        self.name = d["name"]
        self.calorie_goal = d["calorie_goal"]
        self.diary_entries = d["diary_entries"]

    def print_data(self):
        print("Name: {}\nCal Goal: {}\nEntries:".format(self.name, self.calorie_goal))
        for e in self.diary_entries:
            print("\t" + str(e))

    