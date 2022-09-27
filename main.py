# import library mysql
import mysql.connector
import os

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crudpy"
)


def showMenu(db):
    print("--------------------------")
    print("Simple Program With Python")
    print("--------------------------")
    print("1. Input New Data")
    print("2. Show All Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Exit")
    print("--------------------------")
    # take input from user
    choose = input("Choose Menu -> ")

    # clear screen
    os.system("clear")

    # option menu
    if(choose == "1"):
        print("anda pilih 1")
    elif(choose == "2"):
        print("anda pilih 2")
    elif(choose == "3"):
        print("anda pilih 3")
    elif(choose == "4"):
        print("anda pilih 4")
    elif(choose == "5"):
        print("anda pilih 5")
    elif(choose == "0"):
        exit()
    else:
        print("Enter Input Correctly !!!")


# main
if __name__ == "__main__":
    while(True):
        showMenu(db)
