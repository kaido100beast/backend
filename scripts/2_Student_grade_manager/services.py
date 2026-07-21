def find_student(students, name) -> dict:
    return students.get(name, None)

def delete_student(students) -> None:
    try:
        print("Enter student name to delete: ")
        name = input()
        print(f"Student deleted: {students.pop(name, 'Not found')}")
    except ValueError:
        print("Issue deleting student")

def update_student(students) -> None:
    try:
        student = search_student(students)
        print("Enter the subject you want to edit: ")
        edit_subject = input()
        print("Enter new marks: ")
        student[edit_subject] = int(input())
        print("subject marks updated successfully")    
    except ValueError:
        print("Issue updating student")

def search_student(students) -> dict:
    try:
        print("Enter the student name: ")
        name = input()
        student = find_student(students, name)
        if student:
            print(student)
        else:
            print("Student not found")
        return student    
    except ValueError:
        print("Issue searching student")

def add_student(students) -> None:
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

def view_students(students) -> None:
    try:
        for name, subjects in students.items():
            print(f"student: {name}")
            for subject, score in subjects.items():
                print(f"  {subject}: {score}")
            print("Average: ", sum(subjects.values())/len(subjects))
    except ValueError:
        print("Error viewing students")
def highest_scorer(students) -> None:
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