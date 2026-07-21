import json
from constants import JSON_PATH
def import_data(students) -> None:
    try:
        with open(JSON_PATH, 'r') as f:
            students.update(json.load(f))
            return students
        print("Data imported successfully")
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("No existing data found")

def save_data(students) -> None:
    # export to json file
    try:
        with open(JSON_PATH, 'w') as f:
            json.dump(students,f)
        print("Data saved to students.json")
    except OSError:
        print("Error saving data")