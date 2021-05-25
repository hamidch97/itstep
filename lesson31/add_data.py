from create_table import con, cur


def add(table, **value):
    with con:
        cur.execute(f"INSERT INTO {table} VALUES ({value},)")
        print("successfully ")
        


def update_data(table, value, new_value):
    with con:
        cur.execute(f"UPDATE {table} SET {value}={new_value},")
        print("updated successfully ")
        


def delete(value):
    with con:
        cur.execute(f"DELETE FROM 'database.db' WHERE id ={value},")
        print("deleted successfully ")


def menu():
    print("[1]: add element")
    print("[2]: update")
    print("[3]: delete")
    print("[0]: exit")


menu()

if __name__ == "__main__":

    option = int(input("chose an option"))
    while option != 0:

        if option == 1:

            user_table = input("enter name of table")
            user_data = input(
                "enter data here\n beetwen evrey argment put (,),please ")
            add(user_table, **user_data)
            break

        elif option == 2:
            user_table = input("enter name of table")
            user_value = input(" enter value wich you want to change")
            user_new_value = input("enter a new value ")
            update_data(user_table, user_value, user_new_value)
            break

        elif option == 3:
            user_table = int(input("enter position of table"))
            delete(user_table)
            break

        else:
            print("enter correct values please :)")
            break

print("exit")
