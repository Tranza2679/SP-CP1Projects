#Santiago Pineda, Shopping list manager for programming 1!
program_continue = True
good_user_choiceuser_choice = True
shopping_list = []
print("Hello! Welcome to shopping list manager!")
while program_continue:
    while True:
        try:
            add_or_not = str(input("Would you like to add or remove an item from the shopping list? ")).strip().title()
        except:
            print("Please write a good response")
        else:
            break
    good_user_choice = True if add_or_not == "Add" or add_or_not == "Remove" else False
    while not good_user_choice:
        print("Please try again")
        while True:
            try:
                add_or_not = str(input("Would you like to add or remove an item from the shopping list? ")).strip().title()
            except:
                print("Please write a good response")
            else:
                break
        good_user_choice = True if add_or_not == "Add" or add_or_not == "Remove" else False
    if add_or_not == "Add":
        while True:
            try:
                new_item = str(input("What would you like to add? ")).strip().title()
            except:
                print("Please write a good response")
            else:
                break
        shopping_list.append(new_item)
    elif add_or_not == "Remove":
        while True:
            try:
                remove_item = str(input("What would you like to remove? ")).strip().title()
            except:
                print("Please write a good response")
            else:
                break
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
        else:
            print("That item is not in the list, please try again.")
            while True:
                try:
                    remove_item = str(input("What would you like to remove? ")).strip().title()
                except:
                    print("Please write a good response")
                else:
                    break
    while True:
        try:
            show_list = str(input("Would you like to see your current list? Yes or No:  ")).strip().title()
        except:
            print("Please write a good response")
        else:
            break
    good_user_choice_two = True if show_list == "Yes" or show_list == "No" else False
    while not good_user_choice_two:
        print("Please try again")
        while True:
            try:
                show_list = str(input("Would you like to see your current list? Yes or No:  ")).strip().title()
            except:
                print("Please write a good response")
            else:
                break
        good_user_choice_two = True if show_list == "Yes" or show_list == "No" else False
    if show_list == "Yes":
        print(*shopping_list)
    elif show_list == "No":
        continue
    while True:
        try:
            user_input = str(input("Would you like to continue? answer with a yes or no: ")).strip().title()
        except:
            print("Please write a good response")
        else:
            break
    program_continue = True if user_input == "Yes" else False
    