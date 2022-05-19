import mysql.connector
import os

def db_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='BOOKS1',
                                         user='root',
                                         password='tanzil12345')

    sql_select_Query = "select * from Employ"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)

    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")

    for row in records:
        print("Id = ", row[0],)
        print("Name = ", row[1])
        print("Category  = ", row[2], "\n")

# write the data into a text file
    lines = ['Id,Name,Category']
    with open('read.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

    x = open("read.txt",'a')
    print(records,file = x)
    x.close()


db_connection()







