import random
user = int(input("enter number"))

if user < 100:
    user =  random.randint(0,10)


else:
    user = random.randint(0,20)


print(user)
