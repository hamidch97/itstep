try:
    num1 = int(input("enter the first number"))
    mathematical_action = input("wich action would you to do (+,-,*,/)")
    num2 = int(input("enter the second number"))
    final_result = ""
    if mathematical_action == "+":
        final_result = num1 + num2

    if mathematical_action == "-":
        final_result = num1 - num2

    if mathematical_action == "*":
        final_result = num1 * num2
    if mathematical_action == "/":
        final_result = num1 / num2
    print(final_result)
except ZeroDivisionError:
    print("sorry,we can not divide on zero")
except ValueError:
    print("invalid character")
else:
    print("invalid character")
