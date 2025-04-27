from models.student import Student
from models.linked_list import LinkedList

def add_student(list):
    print("\nEntering a new student:")
    id = input("ID: ")
    name = input("Name: ")
    last_name = input("Last Name: ")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    sex = input("Sex: ")
    average = float(input("Average: "))
    student = Student(id, name, last_name, weight, height, sex, average)
    list.add(student)
    return list

def show_list(list):
    current = list.head
    if not current:
        print("The list is empty.")
        return
    while current:
        print(current.student)
        current = current.next
