import menu_item


def show_user_menu():
    while True:
        print("View an Item (V)")
        print("Add an Item (A)")
        print("Delete an Item (D)")
        print("Update an Item (U)")
        print("Show the Menu (S)")
        user_input = input("What is your action? ")
        if user_input.lower() in ['v','a', 'd', 'u', 's', 'x']:
            return user_input
        else:
            print('Choose from the menu please.')


def view_an_item():
    name = input("Please input name of the Dish: ")
    while True:
        price = input("Please insert the price of the Dish: ")
        if not isinstance(price, str):
            print("Input integer please.")
        else:
            break
    return menu_item.MenuItem(name, price)


def add_item_to_menu():
    name = input("Please input name of the Dish: ")
    while True:
        price = input("Please insert the price of the Dish: ")
        if not isinstance(price, str):
            print("Input integer please.")
        else:
            break
    menu_item.MenuItem(name, price).save()
    print(f"{name} was successfully added")


def remove_item_from_menu():
    name = input("Please input name of the Dish: ")
    while True:
        price = input("Please insert the price of the Dish: ")
        if not isinstance(price, str):
            print("Input integer please.")
        else:
            break
    menu_item.MenuItem(name, price).delete()


def show_restaurant_menu():
    for item in menu_item.MenuManager.all_items():
        print(item)


def update_item_from_menu():
    name = input("Please input name of the Dish: ")
    while True:
        price = input("Please insert the price of the Dish: ")
        if not isinstance(price, str):
            print("Input integer please.")
        else:
            break
    new_name = input("Please input new name of the Dish: ")
    while True:
        new_price = input("Please insert the new price of the Dish: ")
        if not isinstance(price, str):
            print("Input integer please.")
        else:
            break
    menu_item.MenuItem(name, price).update(new_name,new_price)


def main():
    while True:
        user_choice = show_user_menu()
        if user_choice == 'x':
            show_restaurant_menu()
            break
        elif user_choice == 'v':
            print(view_an_item())
        elif user_choice == 'a':
            add_item_to_menu()
        elif user_choice == 'd':
            remove_item_from_menu()
        elif user_choice == 'u':
            update_item_from_menu()
        elif user_choice == 's':
            show_restaurant_menu()

main()