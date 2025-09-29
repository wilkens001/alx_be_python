# Initialize the shopping list as a global variable
shopping_list = []

def display_menu():
    """Display the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def main():
    while True:
        # Get the numeric choice from display_menu
        try:
            choice = int(display_menu())
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add an item to the shopping list
            item = input("Enter item name: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == 2:
            # Remove an item from the shopping list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                item = input("Enter item name to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' was not found in the list.")

        elif choice == 3:
            # Display the shopping list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()