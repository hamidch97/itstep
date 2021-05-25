import SQLAlchemy
from phone_table import Phone
from procceseur import Proccesor
from base import engine, Base, session


Base.metadata.create_all(engine)

session = session()


# add phones

phone1 = Phone("samsung","j3",4.4,300)
phone2 = Phone("iphone","7 pro",6.6,1000)
phone3 = Phone("oppo","F1s",5.5,400)
phone4 = Phone("samsung","j5",4.4,350)
phone5 = Phone("samsung","galaxy 5", 4.4,300)

session.add(phone1)
session.add(phone2)
session.add(phone3)
session.add(phone4)
session.add(phone5)

session.commit()
session.close()

#extract phones

mobile = session.query(Phone).all()


def menu():
    print("[1]: draw phone by price")
    print("[2]: draw phone by the name of company")
    print("[3]: see how many phones in the table")
    print("[3]: exit")


menu()
option = int(input("chose an option"))
while option != 0:
    if option == 1:
        print(mobile.price.all())
    elif option == 2:
        print(mobile.company.all())
    elif option == 3:
        print(len(mobile))
    else:
        print("enter the correct values please")
print("exit")
