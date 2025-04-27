import os
import controllers.studentDao as dao
from models.linked_list import LinkedList

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    lista = LinkedList()
    while True:
        print("\n--- MENU ---")
        print("1. Input a student")
        print("2. Display students")
        print("3. Sort students by field")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            clear()
            lista = dao.add_student(lista)
            clear()
            print("Student successfully entered.")
        elif option == "2":
            clear()
            if lista.head:
                dao.show_list(lista)
            else:
                print("No students in the list.")
        elif option == "3":
            clear()
            if lista.head:
                field = input("Enter the field to sort by (id, name, last_name, weight, height, sex, average): ")
                if hasattr(lista.head.student, field):
                    lista = lista.sort_by(field)
                    print(f"List sorted by {field}.")
                else:
                    print("Invalid field.")
            else:
                print("No students in the list.")
        elif option == "4":
            break
        else:
            clear()
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
