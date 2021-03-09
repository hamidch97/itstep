books = ['book1', 'book2', 'book3', 'book4', 'book5']
years = ['2015', '2016', '2017', '2018', '2019']


def menu():
    print("[1]:Book")
    print("[2]:Year")
    print("[3]:Books and years")
    print("[0]:Exit")


menu()
option = int(input("Choose an option"))
res = []
while option != 0:
    if option == 1:
        print(books)
    elif option == 2:
        print(years)
    elif option == 3:
        for i in books:
            for j in years:
                res = [i, j]
            print(res)
    else:
        print("Invalid option")
    option = int(input("Choose an option"))
    menu()
print("Thank you for excuting this progrom.\n GOODBAY")