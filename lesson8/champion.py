# user_input = int(input("enter positive number"))
#
# print(user_input)
# # for i in range(0,len(user_input)):
# #     user_input = int(input("enter positive number"))
# # print(user_input)


NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("The Smallest Element in this List is : ", NumList[0])
print("The Largest Element in this List is : ", NumList[Number - 1])