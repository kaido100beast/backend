import json
Student = {
    "Amar": {
        "Math": 85,
        "Science": 90,
        "English": 78
    },
    "John": {
        "Math": 92,
        "Science": 88,
        "English": 95
    },
    "Max": {
        "Math": 75,
        "Science": 80,
        "English": 70
    }
}
def add_student():
    print("Enter student name: ")
    name = input()
    Student[name] = {}
    print("Enter Math score: ")
    Student[name]["Math"] = int(input())
    print("Enter Science score: ")
    Student[name]["Science"] = int(input())
    print("Enter English score: ")
    Student[name]["English"] = int(input()) 
def view_students():
    for name, subjects in Student.items():
        print(f"Student: {name}")
        for subject, score in subjects.items():
            print(f"  {subject}: {score}")
        print("Average: ", sum(subjects.values())/3)
def highest_scorer():
    highest_score = 0
    highest_student = ""
    for name, subjects in Student.items():
        total_score = sum(subjects.values())
        if total_score > highest_score:
            highest_score = total_score
            highest_student = name
    print(f"Highest Scorer: {highest_student} with a total score of {highest_score}")

def save_data():
    # export to json file
    with open('scripts/day 2/students.json', 'w') as f:
        json.dump(Student,f)
    pass

def main():
    while True:
        print("Welcome to the Student Grade Manager!")
        print("1. Add Student")
        print("2. View Students")
        print("3. Highest Scorer")
        print("4. Save Data")
        print("5. Exit")
        print(" Please select an option (1-5): ")
        input_option = input()
        if input_option == "1":
            add_student()
        elif input_option == "2":
            view_students()
        elif input_option == "3":
            highest_scorer()
        elif input_option == "4":
            save_data()
        elif input_option == "5":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()