user_input = input("enter word here")
inv = user_input[::-1]
if user_input == inv:
    print("true")
else:
    print("false")