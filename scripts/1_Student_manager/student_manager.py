import json
students = {}
def import_data():
    try:
        with open(r'scripts\1_Student_manager\students.json', 'r') as f:
            students.update(json.load(f))
        print("Data imported successfully")
    except FileNotFoundError as e:
        print(f"No existing data found: {e}")

def find_student(name):
    try:
        return students.get(name, {})
    except Exception as e:
        print(f"Issue finding student: {e}")

def delete_student():
    try:
        print("Enter student name to delete: ")
        name = input()
        print(f"Student deleted: {students.pop(name, 'Not found')}")
    except Exception as e:
        print(f"Issue deleting student: {e}")

def update_student():
    try:
        name = search_student()
        for subject,marks in name:
            print(f"Subject: {subject} Marks: {marks}")
        print("Enter the subject you want to edit: ")
        edit_subject = input()
        print("Enter new marks: ")
        students[edit_subject] = input()
        print("subject marks updated successfully")    
    except Exception as e:
        print(f"Issue updating student: {e}")

def search_student():
    try:
        print("Enter the student name: ")
        name = input()
        student = find_student(name)
        if student:
            print("Student found:", name)
            print(student)
        else:
            print("Student not found")
        return student    
    except Exception as e:
        print(f"Issue searching student: {e}")

def add_student():
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
    except Exception as e:
        print(f"Error adding student: {e}")

def view_students():
    try:
        for name, subjects in students.items():
            print(f"students: {name}")
            for subject, score in subjects.items():
                print(f"  {subject}: {score}")
            print("Average: ", sum(subjects.values())/len(subjects))
    except Exception as e:
        print(f"Error viewing students: {e}")
def highest_scorer():
    try:
        highest_score = 0
        highest_student = ""
        for name, subjects in students.items():
            total_score = sum(subjects.values())
            if total_score > highest_score:
                highest_score = total_score
                highest_student = name
        print(f"Highest Scorer: {highest_student} with a total score of {highest_score}")
    except Exception as e:
        print(f"Error calculating highest scorer: {e}")

def save_data():
    # export to json file
    try:
        with open(r'scripts\1_Student_manager\students.json', 'w') as f:
            json.dump(students,f)
        print("Data saved to students.json")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    while True:
        print("Welcome to the students Grade Manager!")
        print("1. Add students")
        print("2. Delete students")
        print("3. update students")
        print("4. search students")
        print("5. View studentss")
        print("6. Highest Scorer")
        print("7. Save Data")
        print("8. Exit")
        print(" Please select an option (1-8): ")
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
