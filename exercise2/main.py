import os
import controllers.route_controller as dao
from models.linked_list import LinkedList

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Definir la ruta de ejemplo
    lista = LinkedList()
    lista.add("Station A", 5)
    lista.add("Station B", 3)
    lista.add("Station C", 7)
    lista.add("Station D", None)  # Última estación

    while True:
        print("\n--- MENU ---")
        print("1. Show stations")
        print("2. Estimate time between stations")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            clear()
            dao.show_list(lista)
        elif option == "2":
            clear()
            dao.calculate_time(lista)
        elif option == "3":
            break
        else:
            clear()
            print("Invalid option. Please try again")

if __name__ == "__main__":
    menu()
