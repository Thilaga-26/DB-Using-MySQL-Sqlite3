import sqlite3

con = sqlite3.connect("Data.db")

def insertData(id,name,age,city):
    sql="insert into users(ID,NAME,AGE,CITY) values ("+id+",'"+name+"','"+age+"','"+city+"')"
    con.execute(sql)
    con.commit()
    con.close()
    print("Inserted Successfully")

def updateData(name,age,city,id):
    sql="update users set name= '"+name+"', age= '"+age+"' ,city= '"+city+"' where id="+id
    con.execute(sql)
    con.commit()
    con.close()
    print("Update Successful")

def deleteData(id):
    sql = "delete from users where id=" +id
    con.execute(sql)
    con.commit()
    print("Deleted successfully")

def displayData():
    sql = "select * from users"
    con.execute(sql)
    result = con.fetchall()
    print(result)
    print("Displayed successfully")

print("""
1.Insert
2.Update
3.Delete
4.Display
""")

ch=1
while ch==1:
    c=int(input("Enter your choice : "))
    if c==1:
        print("Insert Data")
        id = input("Enter your ID : ")
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        city = input("Enter your city : ")
        insertData(id,name,age,city)
    elif c==2:
        print("Update Data")
        id=input("Enter your ID : ")
        name=input("Enter your name : ")
        age=input("Enter your age : ")
        city=input("Enter your city : ")
        updateData(name,age,city,id)
    elif c==3:
        print("Delete Data")
        id=input("Enter your id : ")
        deleteData(id)
    elif c==4:
        print("Display all Data")
        displayData()
    else:
        print("Invalid Choice Entered")
    ch=int(input("Enter 1 to Continue : "))
    print("Thank you")