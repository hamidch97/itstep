first_name = input("enter your first name").upper()
last_name = input("enter your last name").upper()
titel = input("enter titel")
email = str(input("enter your email,example@gmail.com"))
phone_number = "+" + str(input("enter your phone number"))
user_list =[first_name,last_name,titel,email,phone_number]
for i in user_list:
    print(i)