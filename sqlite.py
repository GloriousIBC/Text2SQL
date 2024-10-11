import sqlite3

## Connect to SQLite 
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);  

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute("""Insert into STUDENT values('Krish','Data Science','A',90)""")
cursor.execute("""Insert into STUDENT values('Sudhanshu','Data Science','B',100)""")
cursor.execute("""Insert into STUDENT values('Darius','Data Science','A',86)""")
cursor.execute("""Insert into STUDENT values('Vikash','DEVOPS','A',50)""")
cursor.execute("""Insert into STUDENT values('Dipesh','DEVOPS','A',35)""")

## Display All the records

print("The inserted records are")
data=cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()