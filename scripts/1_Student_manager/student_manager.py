import json
from pathlib import Path
json_path = Path("scripts/1_Student_manager/students.json")
menu = '''
Welcome to the students Grade Manager!
        1. Add students
        2. Delete students
        3. update students
        4. search students
        5. View studentss
        6. Highest Scorer
        7. Save Data
        8. Exit
Please select an option (1-8): '''
students = {}
def import_data() -> None:
    try:
        with open(json_path, 'r') as f:
            students.update(json.load(f))
        print("Data imported successfully")
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("No existing data found")

def find_student(name) -> dict:
    return students.get(name, None)

def delete_student() -> None:
    try:
        print("Enter student name to delete: ")
        name = input()
        print(f"Student deleted: {students.pop(name, 'Not found')}")
    except ValueError:
        print("Issue deleting student")

def update_student() -> None:
    try:
        student = search_student()
        print("Enter the subject you want to edit: ")
        edit_subject = input()
        print("Enter new marks: ")
        student[edit_subject] = int(input())
        print("subject marks updated successfully")    
    except ValueError:
        print("Issue updating student")

def search_student() -> dict:
    try:
        print("Enter the student name: ")
        name = input()
        student = find_student(name)
        if student:
            print(student)
        else:
            print("Student not found")
        return student    
    except ValueError:
        print("Issue searching student")

def add_student() -> None:
    try: 
        print("Enter student name: ")
        name = input()
        students[name] = {}
        num_sub = int(input("Enter the number of subjects: "))
        for i in range(num_sub):
            print(f"Enter subject {i+1} name: ")
            subject = input()
            print(f"Enter score for {subject}: ")
            score = int(input())
            students[name][subject] = score
        print(f"students {name} added successfully")
    except ValueError:
        print("Error adding student")

def view_students() -> None:
    try:
        for name, subjects in students.items():
            print(f"students: {name}")
            for subject, score in subjects.items():
                print(f"  {subject}: {score}")
            print("Average: ", sum(subjects.values())/len(subjects))
    except ValueError:
        print("Error viewing students")
def highest_scorer() -> None:
    try:
        highest_score = 0
        highest_student = ""
        for name, subjects in students.items():
            total_score = sum(subjects.values())/len(subjects)
            if total_score > highest_score:
                highest_score = total_score
                highest_student = name
        print(f"Highest Scorer: {highest_student} with a total score of {highest_score}")
    except ValueError:
        print("Error calculating highest scorer")

def save_data() -> None:
    # export to json file
    try:
        with open(json_path, 'w') as f:
            json.dump(students,f)
        print("Data saved to students.json")
    except OSError:
        print("Error saving data")

def main():
    while True:
        print(menu)
        input_option = input()
        if input_option == "1":
            add_student()
        elif input_option == "2":
            delete_student()
        elif input_option == "3":
            update_student()
        elif input_option == "4":
            search_student()
        elif input_option == "5":
            view_students()
        elif input_option == "6":
            highest_scorer()
        elif input_option == "7":
            save_data()
        elif input_option == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    import_data()
    main()
