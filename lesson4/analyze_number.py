try:
    num = int(input("enter number"))
    # it's the rest of num/2
    r = num % 2
    if num > 0:
        print(num, "is a positive number")
    if num < 0:
        print(num, "is a negative number")
    if num == 0:
        print(num, "is Neutral number")
    if r == 0:
        print(num, "is even")
    if r != 0:
        print(num, " is not even")
except ValueError:
    print("only numbers please")
else:
    print("only numbers please")
