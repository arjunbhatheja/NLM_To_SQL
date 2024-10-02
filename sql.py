import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Alice','Machine Learning','A',92)''')
cursor.execute('''Insert Into STUDENT values('Bob','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('Charlie','Cyber Security','A',85)''')
cursor.execute('''Insert Into STUDENT values('David','DEVOPS','B',67)''')
cursor.execute('''Insert Into STUDENT values('Eve','Cloud Computing','A',88)''')
cursor.execute('''Insert Into STUDENT values('Fiona','Artificial Intelligence','B',95)''')
cursor.execute('''Insert Into STUDENT values('George','Machine Learning','A',74)''')
cursor.execute('''Insert Into STUDENT values('Hannah','Cyber Security','B',82)''')
cursor.execute('''Insert Into STUDENT values('Ian','DEVOPS','A',63)''')
cursor.execute('''Insert Into STUDENT values('Jenna','Cloud Computing','B',90)''')


## Display all the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()