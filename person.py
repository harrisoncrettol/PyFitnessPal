from datetime import datetime
from diary_entry import DiaryEntry
import json

class User:
    def __init__(self, name=None, password=None, cal_goal=None):
        self.name = name
        self.password = password
        self.calorie_goal = cal_goal
        self.diary_entries = []


    # returns bool indicating if entry exists for that day
    def has_entry(self, date) -> bool:
        for e in self.diary_entries:
            if date in e.keys():
                return True
        return False


    # returns dict version of DiaryEntry for that day
    # precondition: entry must exist for that day
    def get_entry(self, date) -> dict:
        for e in self.diary_entries:
            if date in e.keys():
                return e
        return DiaryEntry(date).to_dict()


    # returns dict version of obj
    def to_dict(self) -> dict:
        return {"name": self.name, "password": self.password, "calorie_goal": self.calorie_goal, "diary_entries": self.diary_entries}


    # writes user data as a json string to an output file
    def write_data(self) -> None:
        if self.is_default():
            return None
        
        with open(self.get_filename(), "w") as f:
            f.write(json.dumps(self.to_dict()))


    # reads user data (json string) from a file into the User obj
    def load_data(self) -> None:
        with open(self.get_filename(), "r") as f:
            data = f.read()
            
        d = json.loads(data)
        self.name = d["name"]
        self.password = d["password"]
        self.calorie_goal = d["calorie_goal"]
        self.diary_entries = d["diary_entries"]

    # returns True if user has not updated their data
    def is_default(self) -> bool:
        return not (bool(self.name) and bool(self.password) and bool(self.calorie_goal))


    # prints the user's data
    def show_data(self) -> None:
        print("Name: {}\nCalorie Goal: {}\nEntries:".format(self.name, self.calorie_goal))
        for e in self.diary_entries:
            print("\t" + str(e))


    def get_filename(self):
        return "users//{}_{}.txt".format(self.name, self.password)

# Prompts user for name and cal goal
# Returns User obj with that data
def create_user() -> User:
    name = input("Enter your name: ")
    password = input("Enter a password: ")
    cal_goal = input("Enter your calorie goal: ")
    user = User(name, password, cal_goal)
    user.write_data()
    return user

    