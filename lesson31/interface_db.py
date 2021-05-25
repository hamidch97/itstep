from create_table import con, cur


def menu():
    print("[1]: Displaying all trades ")
    print("[2]: Displaying a particular seller's trades ")
    print("[3]: Displaying the maximum amount of the transaction")
    print("[4]: Displaying the minimum amount of the transaction")
    print("[5]: Displaying the maximum amount of the transaction for The seller's specific one")
    print("[6]: Displaying the minimum amount of the transaction for The seller's specific one")
    print("[7]: Displaying the maximum amount of the transaction for A specific buyer")
    print("[8]: Displaying the minimum amount of the transaction for A specific buyer")
    print("[9]: Showing the saller with the maximum amount of purchases for all transactions.")
    print("[10]: Showing the buyer with the maximum amount of purchases for all transactions.")
    print("[0]: exit")


menu()
option = None
while option != 0:
    option = int(input("choose an option"))

    if option == 1:
        cur.execute("SELECT*FROM 'sales'")

    elif option == 2:
        saller = input("enter saller name")
        cur.execute(
            "SELECT trades FROM 'salesmans'  WHERE nikname=(?)", (saller,))

    elif option == 3:
        saller = input("enter saller name")
        cur.execute("SELECT MAX(tansaction), tansactions FROM 'sales'")

    elif option == 4:
        cur.execute("SELECT MIN(tansaction), tansactions FROM 'sales'")

    elif option == 5:
        saller = input("enter saller name")
        cur.execute(
            "SELECT MAX(tansaction), tansactions FROM 'salesman' WHERE nikname=(?)", (saller,))

    elif option == 6:
        saler = input("enter saller name")
        cur.execute(
            "SELECT MIN(tansaction), tansactions FROM 'salesman' WHERE nikname=(?)", (saller,))

    elif option == 7:
        bayer = input("enter bayer name")
        cur.execute(
            "SELECT Max(tansaction), tansactions FROM 'constumers' WHERE nikname=(?)", (bayer,))

    elif option == 8:
        bayer = input("enter bayer name")
        cur.execute(
            "SELECT MIN(tansaction), tansactions FROM 'constumers' WHERE nikname=(?)", (bayer,))

    elif option == 9:
        cur.execute("SELECT MAX(transactions),transactions FROM 'salesmans'")
        print("done")

    elif option == 10:
        cur.execute("SELECT MAX(transaction),transactions FROM 'constumers'")

    else:
        print("check your data")


print("back")
