import os
import controllers.patient_controller as c

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clinic_queue = []

    while True:
        print("\n--- MENU ---")
        print("1. Add new patient")
        print("2. Show patient list")
        print("3. Attend next patient")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            clear()
            name = input("Full name: ")
            try:
                age = int(input("age: "))
                if age <= 0:
                    clear()
                    print("Must be >0.")
                    continue
            except ValueError:
                clear()
                print("Invalid age")
                continue
            symptom = input("Main symptom: ")
            try:
                priority = int(input("Priority (1 to 5): "))
                if not 1 <= priority <= 5:
                    clear()
                    print("Priority must be from 1 to 5")
                    continue
            except ValueError:
                clear()
                print("Invalid priority")
                continue
            
            c.add_patient(clinic_queue, name, age, symptom, priority)
            clear()
            print("Added patient succesfully")

        elif option == "2":
            clear()
            c.show_queue(clinic_queue)

        elif option == "3":
            clear()
            c.attend_patient(clinic_queue)

        elif option == "4":
            print("Logging out")
            break

        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()
