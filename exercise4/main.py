import os
import controllers.action_controller as ac

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    history = []
    redo_stack = []

    while True:
        print("\n--- MENU ---")
        print("1. Perform action")
        print("2. Undo action")
        print("3. Redo action")
        print("4. Show history")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            clear()
            action = input("Enter action (write, delete, copy, paste): ")
            ac.add_action(history, redo_stack, action)
            clear()
            print(f"Action '{action}' added successfully.")
        elif choice == "2":
            clear()
            ac.undo_action(history, redo_stack)
        elif choice == "3":
            clear()
            ac.redo_action(history, redo_stack)
        elif choice == "4":
            clear()
            ac.show_history(history)
        elif choice == "5":
            clear()
            print("Exiting action history.")
            break
        else:
            clear()
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
