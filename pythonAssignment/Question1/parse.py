import csv
import pymysql

filename = "Delimeter1.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))
    print('Field names are:' + ', '.join(field for field in fields))
    print('\n The rows are:\n')
    for row in rows[:100]:
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')

def db_connection(query):
    
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "tanzil12345",
        db='mysql',
        )

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if len(row) > 0:
                query = '''"INSERT INTO Employe(ID,Firstname,Lastname,Gender,Salary,DOB)
                 VALUES  ({},'{}','{}','{}',{},'{}')".
                format(row[0], row[1], row[2], row[3], row[4], row[5])'''
                print(query)

            db_connection(query)












