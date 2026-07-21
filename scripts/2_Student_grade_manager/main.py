from constants import MENU
from storage import import_data, save_data
from services import add_student, delete_student, update_student, search_student, view_students, highest_scorer
def main():
    students = {}
    students = import_data(students)
    while True:
        print(MENU)
        input_option = input()
        if input_option == "1":
            add_student(students)
        elif input_option == "2":
            delete_student(students)
        elif input_option == "3":
            update_student(students)
        elif input_option == "4":
            search_student(students)
        elif input_option == "5":
            view_students(students)
        elif input_option == "6":
            highest_scorer(students)
        elif input_option == "7":
            save_data(students)
        elif input_option == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()