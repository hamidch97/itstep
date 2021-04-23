def email_validation(x):
    a=0
    y=len(x)
    dot=x.find(".")
    at=x.find("@")
    for i in range (0,at):
        if((x[i]>='a' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
            a=a+1
    if(a>0 and at>0 and (dot-at)>0 and (dot+1)<y):
        pass
    else:
        print("Invalid Email")

def number_validation(n):
    for i in len(n+1):
        if n[0:4] == "+"+int("380") and isinstance(n[4:13],int):
            pass
        else:
            print("phone number must be  intger")

first_name = input("enter your first name")
last_name = input("enter your last name")
titel = input("enter titel")
email = str(input("enter your email,example@gmail.com"))
phone_number = "+" + str(input("enter your phone number"))
data_list =[first_name,last_name,titel,email,phone_number]
runnig = True
while runnig:
    for i in data_list:
        if isinstance(first_name,str)  or first_name.upper:
            data_list.append(i)
        elif isinstance(last_name,str) or last_name.upper:
            data_list.append(i)  
        elif isinstance(titel ,str) or titel.upper:
            data_list.append(i)
        elif  email_validation(email):
            data_list.append(i)
        elif number_validation(phone_number):
            data_list.append(i)
        runnig =False
    first_name = input("enter your first name")
    last_name = input("enter your last name")
    titel = input("enter titel")
    email = str(input("enter your email,example@gmail.com"))
    phone_number = "+" + str(input("enter your phone number"))
    


print(user_list)
        