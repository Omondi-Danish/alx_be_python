#Creating an empty shopping list then promping the user to add, remove or update items of the list

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. remove item")
    print("3. view list")
    print("4. exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")
        elif choice == "2":
            item = input("Enter item to remove: ").strip()
            shopping_list.remove(item)
            print(f"{item} removed from the shopping list")
        elif choice == "3":
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("🛒 Your shopping list is empty.")
        elif choice == '4':
            print("👋 Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("❗ Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()