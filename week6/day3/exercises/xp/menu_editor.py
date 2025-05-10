from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Restaurant Menu Editor ---")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show Full Menu")
        print("E - Exit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'V':
            name = input("Enter item name: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name} - ${item.price}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("\nFinal Menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Try again.")

def add_item_to_menu():
    name = input("Enter item name to add: ")
    try:
        price = int(input("Enter item price: "))
        item = MenuItem(name, price)
        item.save()
        print("Item was added successfully.")
    except Exception as e:
        print("Error adding item:", e)

def remove_item_from_menu():
    name = input("Enter item name to delete: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item deleted successfully.")
    else:
        print("Item not found. Nothing deleted.")

def update_item_from_menu():
    current_name = input("Enter current item name: ")
    item = MenuManager.get_by_name(current_name)
    if item:
        new_name = input("Enter new item name: ")
        try:
            new_price = int(input("Enter new price: "))
            item.update(new_name, new_price)
            print("Item updated successfully.")
        except Exception as e:
            print("Update failed:", e)
    else:
        print("Item not found. Update aborted.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("Menu is empty.")
    else:
        print("\n--- Restaurant Menu ---")
        for item in items:
            print(f"{item.name} - ${item.price}")
