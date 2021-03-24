
# create menu

def menu():
    print("[1] : view taskes")
    print("[2] : add taskes")
    print("[3] : change taskes ")
    print("[4] : mark taskes done")
    print("[5] : delete taskes")
    print("[0] : exit")


menu()

# create a ToDo list

todo_list = [
    "call frind",
    "visit a doctor"
]
option = int(input("choose an option"))
while option != 0:
    if option == 1:
        for i in todo_list:
            print(i)
        break
    elif option == 2:
        add_task = ""
        while add_task != "exit":
            add_task = input("enter a new task ,\n enter exit to exit to menu")
            todo_list.append(add_task)
        menu()
        option = int(input("choose an option"))

    elif option == 3:
        change_task = input("which task would you change")
        update_task = input("enter new task")
        for i in todo_list:
            if i == change_task:
                todo_list[i] = todo_list[update_task]
            else:
                print("soory ,you didn't write this taske already ")
    elif option == 4:
        done_taskes = input("enter task which would you mark like done")
        for i in todo_list:
            if i == done_taskes:
                [todo_list][i] = "\u2713" + [todo_list][i]
        print(todo_list)

    elif option == 5:
        del_task = input("whish task would you want to delete")
        if del_task in todo_list:
            todo_list -= todo_list[del_task]
        print(todo_list)

    else:
        print("option not valid")

    menu()
    option = int(input("choose an option"))

print("thank you for using this programme")
