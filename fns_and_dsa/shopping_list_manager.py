def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print()

def main():
    print("#####Welcome to the Shopping List Manager#####")
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            item_present = 0
            if item:
                if bool(shopping_list):
                    for i in shopping_list:
                        if i == item:
                            item_present = 1
                            print(f"{item} is already on the list.")
                            break
                    if item_present == 0:
                        shopping_list.append(item)
                        print(f"{item} has been successfully added to the shopping list.")
                    else:
                        continue
                else:
                    shopping_list.append(item)
                    print(f"{item} has been successfully added to the shopping list.")
            else:
                print("Item name is required.")
            print()
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item:
                if bool(shopping_list) == True:
                    for i in shopping_list:
                        if i == item:
                            shopping_list.remove(item)
                            print(f"{item} has been successfully removed from the shopping list.")
                            break
                    print(f"{item} is not on your list.")
                else:
                    print("There are no items on your list.")
            else:
                print("Item name is required.")
            print()
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                index = 1
                for item in shopping_list:
                    print(f"{index}. {item}")
                    index += 1
            else:
                print("Your shopping list is empty.")
            print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()