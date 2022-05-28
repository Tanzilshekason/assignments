import psycopg2

#  Database Connection
def my_function():
    mydb = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "root",
        database = "books"
    )

    mycursor = mydb.cursor()

    # For table category Employ
    mycursor.execute('''CREATE TABLE Employ(Id INT,
    emp_Name Varchar(255),emp_bookname VARCHAR(255),
    book_category VARCHAR(255))''')
    query = "INSERT INTO Employ(Id,emp_Name,emp_bookname,book_category) VALUES(%s,%s,%s,%s)"
    b1 = (1,'David','Life Of Pie','Action And Adventure')
    b2 = (2,'Tim','The Call Of The Wild','Action And Adventure')
    b3 = (3,'John','To Kill A MockingBird','Classics')
    b4 = (4,'Selvin','Little Women','Classics')
    b5 = (5,'Maxwell','The Avengers','Comic')
    b6 = (6,'Rohit','X-MEN','Comic')
    b7 = (7,'Virat','The Whistler','Mystery')
    b8 = (8,'Sarah','Game Of Thrones','Fantasy')
    b9 = (9,'Lily','Dracula','Horror')
    b10 = (10,'Dhoni','The Tell-Tale Heart','Horror')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mycursor.execute(query,b7)
    mycursor.execute(query,b8)
    mycursor.execute(query,b9)
    mycursor.execute(query,b10)
    mydb.commit()
    mycursor.execute("SELECT * FROM Employ")
    for db in mycursor:
        print(db)



    # For Table Category student
    mycursor.execute('''CREATE TABLE student(Id INT,
    stu_Name VARCHAR(255),stu_bookname VARCHAR(255),
    category VARCHAR(255))''')
    query = "INSERT INTO student(Id,stu_Name,stu_bookname,category) VALUES(%s,%s,%s,%s)"
    b1 = (1,'Ponting','Heart Of Darkness','Action And Adventure')
    b2 = (2,'Ellyse','Tarzan Of The Apes','Action And Adventure')
    b3 = (3,'Rose','Vintage Beloved','Classics')
    b4 = (4,'Taylor','I Capture The Castle','Classics')
    b5 = (5,'Robbert','Batman','Comic')
    b6 = (6,'Jacob','The Amazing Spider-Man','Comic')
    b7 = (7,'Bella','The Woman In White','Mystery')
    b8 = (8,'Justin','Vampire Academy','Fantasy')
    b9 = (9,'Mary','World War Z','Horror')
    b10 = (10,'Shane','The Hunger','Horror')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mycursor.execute(query,b7)
    mycursor.execute(query,b8)
    mycursor.execute(query,b9)
    mycursor.execute(query,b10)
    mydb.commit()
    mycursor.execute("SELECT * FROM student")
    for db in mycursor:
        print(db)
    
my_function()