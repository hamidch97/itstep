import json


class Employees:

    def __init__(self, first_name, last_name, titel, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.titel = titel
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"first name:text{self.first_name}\nlast name: {self.last_name}\ntitel: {self.titel}\nemail: {self.email}\nphone numbers: {self.phone_number}"

    def string_validation(self):
        if isinstance(self.first_name, str) and isinstance(self.last_name, str) and isinstance(self.titel, str):
            pass
        else:
            print("enter correct value(first name,last name,titel)")

    @staticmethod
    def email_validation(x):
        charachters = [
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ.-_0123456789"]
        email_examples = [
            "gmail.com",
            "yahoo.com",
            "hotmail.com",

        ]

        at = x.find("@")
        for i in len(x)+1:
            if x[0:at] in charachters and x[at:len(x)+1] in email_examples:
                pass
        else:
            print("Invalid Email")

    @staticmethod
    def number_validation(n):
        if isinstance(n, int) and len(n) == 9:
            pass
        else:
            print("enter correct number please")

    def save_data(self):
        dictt = {"first name": self.first_name,
                 "last name": self.last_name,
                 "titel": self.titel,
                 "email": self.email,
                 "phone number": ("+380" + self.phone_number)
                 }

        while bool(emp.string_validation) is True and bool(emp.email_validation) is True and bool(emp.number_validation) is True:
            with open("mydata.json", "w") as f:
                array = json.dump(dictt, f)
                print("succsfuly")
                break
        else:
            print("check your data")


if __name__ == "__main__":
    running = True
    while running:
        user = input(
            "enter next if you want to continue\ntape exit if you want to exit ")

        if user == "next":
            input_name = input("enter first name ")
            input_last_name = input("enter last name ")
            input_titel = input("enter titel ")
            input_email = input("enter email ")
            input_num = input("enter number\n+380--------- ")
            emp = Employees(input_name, input_last_name,
                            input_titel, input_email, input_num)

        elif user == "exit":
            emp.save_data()
            running = False
        else:
            print("enter the corect value please\n*********************")

    print("thank you for using this programme :)")
