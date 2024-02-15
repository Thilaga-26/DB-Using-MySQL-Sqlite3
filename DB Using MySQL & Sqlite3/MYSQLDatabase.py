import mysql.connector
con=mysql.connector.connect(host="localhost", user="root", password="Lanasri@26", database="py")

def insertData(name,age,city):
    res=con.cursor()
    sql="insert into users(NAME,AGE,CITY) values (%s,%s,%s)"
    res.execute(sql,(name,age,city))
    con.commit()
    print("Inserted Successfully")

def updateData(name,age,city,id):
    res=con.cursor()
    sql="update users set name=%s, age=%s, city=%s where id=%s"
    res.execute(sql, (name,age,city,id))
    con.commit()
    print("Update Successful")

def deleteData(id):
    res=con.cursor()
    sql = "delete from users where id=%s"
    res.execute(sql, (id,))
    con.commit()
    print("Deleted successfully")

def displayData():
    res=con.cursor()
    sql = "select * from users"
    res.execute(sql)
    result = res.fetchall()
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
        name=input("Enter your name : ")
        age=input("Enter your age : ")
        city=input("Enter your city : ")
        insertData(name,age,city)
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