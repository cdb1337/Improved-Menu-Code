USER_CHOICE = """
-> Press "N" to add new item 
-> Press "V" to view all items
-> Press "S" to select each item in the menu
-> Press "D" to delete the selected item
-> Press "Q" to quit
"""

def new_item():
    pass

def view_items():
    pass

def select_item():
    pass

def delete_item():
    pass

user_choices = {
        "N": new_item,
        "V": view_items,
        "S": select_item,
        "D": delete_item,
    }

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "Q":
        if user_input in ("N", "V", "S", "D"):
            user_choices[user_input]()
        else:
            print("Choose a valid command.")
        user_input = input(USER_CHOICE)


menu()
