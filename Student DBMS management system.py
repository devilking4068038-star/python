import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password")
cursor = conn.cursor()
def add_database():
    x = input("Enter your DB name: ")
    cursor.execute(f"CREATE DATABASE `{x}`")
    print("Database created successfully")
def del_database():
    x = input("Enter your DB name: ")
    cursor.execute(f"DROP DATABASE `{x}`")
    print("Database deleted successfully")
def create_table():
    n = input("Enter your database name: ")
    cursor.execute(f"USE `{n}`")
    x = input("Enter your table name: ")
    cursor.execute(f"CREATE TABLE `{x}` (id INT AUTO_INCREMENT PRIMARY KEY)")
    y = input("Do you want to add columns? (yes/no): ")
    while y.lower() == "yes":
        constraints = input("Enter column definition (e.g., name VARCHAR(50)): ")
        cursor.execute(f"ALTER TABLE `{x}` ADD {constraints}")
        y = input("Add more columns? (yes/no): ")
    print("Table created successfully")
def add_table_data():
    n = input("Enter your database name: ")
    cursor.execute(f"USE `{n}`")
    x = input("Enter your table name: ")
    y = input("Do you want to add data? (yes/no): ")
    while y.lower() == "yes":
        a = int(input("How many columns do you want to add data for? "))
        columns = []
        data = []
        for i in range(a):
            b = input("Enter column name: ")
            c = input("Enter column data: ")
            columns.append(b)
            data.append(c)
        column_names = ", ".join([f"`{col}`" for col in columns])
        placeholders = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO `{x}` ({column_names}) VALUES ({placeholders})"
        cursor.execute(query, data)
        print("One row inserted successfully")
        y = input("Add more data? (yes/no): ")
def del_table():
    n = input("Enter your database name: ")
    cursor.execute(f"USE `{n}`")
    x = input("Enter your table name: ")
    z = input("Enter your choice what you want to delete (1: entire table / 2: column): ")
    if z == "1":
        cursor.execute(f"DROP TABLE `{x}`")
        print("Table deleted successfully")
    elif z == "2":
        y = input("Do you want to delete a column from table? (yes/no): ")
        while y.lower() == "yes":
            a = input("Enter your column name: ")
            cursor.execute(f"ALTER TABLE `{x}` DROP COLUMN `{a}`")
            print(f"Column '{a}' deleted successfully")
            y = input("Delete more columns? (yes/no): ")
def fetch_data():
    n = input("Enter your database name: ")
    cursor.execute(f"USE `{n}`")
    x = input("Enter your table name: ")
    z = input("Enter choice (1: entire table / 2: specific columns / 3: with conditions): ")
    if z == "1":
        cursor.execute(f"SELECT * FROM `{x}`")
    elif z == "2":
        a = int(input("How many columns to fetch: "))
        column = []
        for i in range(a):
            b = input("Enter column name: ")
            column.append(f"`{b}`")
        columns = ", ".join(column)
        cursor.execute(f"SELECT {columns} FROM `{x}`")
    elif z == "3":
        conditions = []
        ch = input("Do you want to add conditions? (yes/no): ")
        while ch.lower() == "yes":
            b = input("Enter condition (e.g., age > 18): ")
            conditions.append(b)
            ch = input("Add more conditions? (yes/no): ")
        if conditions:
            where_clause = " AND ".join(conditions)
            cursor.execute(f"SELECT * FROM `{x}` WHERE {where_clause}")
        else:
            cursor.execute(f"SELECT * FROM `{x}`")

    results = cursor.fetchall()
    for row in results:
        print(row)
n = input("Enter your choice to start (yes/no): ")
while n.lower() == "yes":
    t = int(input(
        "Enter your choice "
        "(1: add database / 2: delete database / 3: create table / "
        "4: delete table / 5: fetch data / 6: add table data): "
    ))
    if t == 1:
        add_database()
    elif t == 2:
        del_database()
    elif t == 3:
        create_table()
    elif t == 4:
        del_table()
    elif t == 5:
        fetch_data()
    elif t == 6:
        add_table_data()
    else:
        print("Invalid choice")
    conn.commit()
    n = input("Do you want to continue? (yes/no): ")
cursor.close()
conn.close()
