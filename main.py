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


# insert data to database
def insertData(db):
    name = input("Enter Name    : ")
    address = input("Enter Address : ")
    major = input("Enter Major   : ")
    value = (name, address, major)
    # execute statements to communicate with the MySQL database
    cursor = db.cursor()
    sql = "INSERT INTO mahasiswapy (nama, alamat, jurusan) VALUES (%s, %s, %s)"
    cursor.execute(sql, value)
    # commit statement sql
    db.commit()
    print("{} Data Added Successfully".format(cursor.rowcount))


# show data from database
def showData(db):
    cursor = db.cursor()
    sql = "SELECT * FROM mahasiswapy"
    cursor.execute(sql)
    # fetchall()    -> take all data from database
    # fetchmany(10) -> take 10 data from database
    # fetchone()    -> take first data only
    # with the above function,the data list will be returned as a tuple
    dataDb = cursor.fetchall()

    # check if data is empty
    if cursor.rowcount < 0:
        print("Data is empty")
    else:
        for data in dataDb:
            print(data)


# update data from database
def updateData(db):
    cursor = db.cursor()
    # show data first to see where data must be update
    showData(db)
    print("===================================")
    # take new data from user
    customerId = input("Enter Id -> ")
    name = input("Enter New Name    : ")
    address = input("Enter New Address : ")
    major = input("Enter New Major   : ")

    sql = "UPDATE mahasiswapy SET nama = %s, alamat = %s, jurusan = %s WHERE id = %s"
    value = (name, address, major, customerId)
    # execute statements to communicate with the MySQL database
    cursor.execute(sql, value)
    # commit statement sql
    db.commit()
    print("{} Data Updated Successfully".format(cursor.rowcount))


# delete data from database
def deleteData(db):
    cursor = db.cursor()
    # show data before data has be delete
    showData(db)
    idDb = input("Choose the Id you want delete -> ")
    sql = "DELETE FROM mahasiswapy WHERE id = %s"
    value = (idDb, )
    # execute statements to communicate with the MySQL database
    cursor.execute(sql, value)
    # commit statement sql
    db.commit()
    print("{} Data Deleted Successfully".format(cursor.rowcount))


# search data from database
def searchData(db):
    cursor = db.cursor()
    # take the keyword for searching
    keyword = input("Enter Keyword -> ")
    sql = "SELECT * FROM mahasiswapy WHERE nama LIKE %s OR alamat LIKE %s OR jurusan LIKE %s"
    value = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
    # execute statements to communicate with the MySQL database
    cursor.execute(sql, value)
    result = cursor.fetchall()

    # check data found or not
    if cursor.rowcount < 0:
        print("Data Not Found")
    else:
        for data in result:
            print(data)


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
    os.system("cls")

    # option menu
    if(choose == "1"):
        insertData(db)
    elif(choose == "2"):
        showData(db)
    elif(choose == "3"):
        updateData(db)
    elif(choose == "4"):
        deleteData(db)
    elif(choose == "5"):
        searchData(db)
    elif(choose == "0"):
        exit()
    else:
        print("Enter Input Correctly !!!")


# main
if __name__ == "__main__":
    while(True):
        showMenu(db)
