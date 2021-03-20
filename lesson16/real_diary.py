def menu():
    print("[1]:VIEW TASKES")
    print("[2]:ADD TASKES")
    print("[3]:DELETE TASKS")
    print("[0]:EXIT")


menu()

taskes_day = {
    "monday": ("homework", "call mom"),
    "theusday": ("work", "call friend"),
    "wednesday": "work",
    "thursday": "work",
    "freeday": "work",
    "sunday": "work",
    "saturday": "work",
}

user = int(input("enter your option"))
while user != 0:
    user_option = ""
    if user == 1:
        user_option = input("enter day")
        print(taskes_day.setdefault(user_option))

    elif user == 2:
        day = input("enter day where would you put your new taske")
        user_option = input("enter new taske ")
        taskes_day[day] = taskes_day[day] + tuple(user_option.split(","))
        print(taskes_day)

    elif user == 3:
        user_option = input("which taskes would you delete? ")
        for elem in taskes_day.items():
            if user_option == elem:
                taskes_day -= taskes_day[user_option]
        print(taskes_day)
    else:
        print("option invalide")

    user = int(input("enter your option"))

print("thank you for using this programme, good-bay")
