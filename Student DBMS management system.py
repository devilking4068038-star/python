import mysql.connector
def adddatabse():
    x=input("enter your DB name:")
    cursor.execute("create database {}".format(x))
def deldatabse():
    x=input("enter your DB name")
    cursor.execute("drop databse {}".format(x))
def createtable():
    x=input("enter your table name:")
    cursor.execute("create table {}".format(x))
    y=input("enter your choice to add column and constraints in table(yes/no):")
    while y=="yes":
        constraints=input("enter your column name and constraint you want to add:")
        cursor.execute("alter table {} add {}".format(x,constraints))
    return print("Table created successfully")
def deltable():
    x=input("enter your table name:")
    z=int(input("enter your choice what you want to delete(1:- for entire table/2:- for column:"))
    if z=="1":
        cursor.execute("drop table {}".format(x))
    elif z=="2":
        y=input("enter your choice to delete column from table(yes/no):")
        while y=="yes":
            a=input("enter your column name:")
            cursor.execute("ALTER TABLE {} DROP COLUMN {};".format(x,a))
def fetchdata():
    x=input("enter your table name:")
    z=input("enter your choice to fetch data from table"
            "(1:- to fetch entire table/2:- to fetch specific column/3:- to fetch with conditions):")
    if z=="1":
        cursor.execute("select * from {}".format(x))
    elif z=="2":
        a=int(input("enter how many column you want to fetch:"))
        column=[]
        for i in range(a):
            b=input("enter your column name:")
            column.append(b)
        cursor.execute("select {} * from {}".format(column,x))
    elif z=="3":
        n=input("enter your choice for conditions(yes/no):")
        while n=="yes":
            b=input("enter your column conditions:")
        cursor.execute("select * from {} where {} and {}".format(x,b,b))

conn = mysql.connector.connect(host="localhost",user="root",password="password",)
cursor = conn.cursor()
n=input("enter your choice(yes/no):")
while n=="yes":
    t=int(input("enter your choice"
                "(1:- to add database/2:-delete database/3:- create table"
                "/4:= delete table/5:-fetch data):"))
    if t==1:
        adddatabse()
    elif t == 2:
        deldatabse()
    elif t == 3:
        createtable()
    elif t == 4:
        deltable()
    elif t == 5:
        fetchdata()
