import psycopg2
 
def db_connection():
    mydb = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "root",
        database = "books"
    )

    mycursor = mydb.cursor()



    # For Table Action Category
    mycursor.execute("CREATE TABLE Action(ID INT,BOOKNAME VARCHAR(255),CATEGORY VARCHAR(255))")
    query = "INSERT INTO Action(ID,BOOKNAME,CATEGORY) VALUES(%s,%s,%s)"
    b1 = (1,'Life Of Pie','Action And Adventure')
    b2 = (2,'The Call Of The Wild','Action And Adventure')
    b3 = (3,'Heart Of Darkness','Action And Adventure')
    b4 = (4,'Tarzan Of The Apes','Action And Adventure')
    b5 = (5,'The jungle Book','Action And Adventure')
    b6 = (6,'The Cruel Sea','Action And Adventure')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mydb.commit()
    mycursor.execute("SELECT * FROM Action")
    for db in mycursor:
        print(db)



    # For Table Category Classics
    mycursor.execute("CREATE TABLE Classics(ID INT,BOOKNAME VARCHAR(255),CATEGORY VARCHAR(255))")
    query = "INSERT INTO Classics(ID,BOOKNAME,CATEGORY) VALUES(%s,%s,%s)"
    b1 = (1,'To Kill A MockingBird','Classics')
    b2 = (2,'Little Women','Classics')
    b3 = (3,'Vintage Beloved','Classics')
    b4 = (4,'I Capture The Castle','Classics')
    b5 = (5,'Jane Eyre','Classics')
    b6 = (6,'The Call Of The Wild','Classics')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mydb.commit()
    mycursor.execute("SELECT * FROM Classics")
    for db in mycursor:
        print(db)



    # For Table Category Comic Book
    mycursor.execute("CREATE TABLE ComicBook(ID INT,BOOKNAME VARCHAR(255),CATEGORY VARCHAR(255))")
    query = "INSERT INTO ComicBook(ID,BOOKNAME,CATEGORY) VALUES(%s,%s,%s)"
    b1 = (1,'The Avengers','Comic')
    b2 = (2,'X-MEN','Comic')
    b3 = (3,'Batman','Comic')
    b4 = (4,'The Amazing Spider-Man','Comic')
    b5 = (5,'The Incredible Hulk','Comic')
    b6 = (6,'Wolverine','Comic')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mydb.commit()
    mycursor.execute("SELECT * FROM ComicBook")
    for db in mycursor:
        print(db)



    # For Table Category Mystery
    mycursor.execute("CREATE TABLE Mystery(ID INT,BOOKNAME VARCHAR(255),CATEGORY VARCHAR(255))")
    query = "INSERT INTO Mystery(ID,BOOKNAME,CATEGORY) VALUES(%s,%s,%s)"
    b1 = (1,'The Whistler','Mystery')
    b2 = (2,'The Woman In White','Mystery')
    b3 = (3,'The Eye Of The Beholder','Mystery')
    b4 = (4,'Sneaky People','Mystery')
    b5 = (5,'A Simple plan','Mystery')
    b6 = (6,'In Cold Blood','Mystery')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mydb.commit()
    mycursor.execute("SELECT * FROM Mystery")
    for db in mycursor:
        print(db)



# For Table Fantasy  
    mycursor.execute("CREATE TABLE Fantasy(ID INT,BOOKNAME VARCHAR(255),CATEGORY VARCHAR(255))")
    query = "INSERT INTO Fantasy(ID,BOOKNAME,CATEGORY) VALUES(%s,%s,%s)"
    b1 = (1,'Game Of Thrones','Fantasy')
    b2 = (2,'The Way Of Kings','Fantasy')
    b3 = (3,'American Gods','Fantasy')
    b4 = (4,'The Night Circus','Fantasy')
    b5 = (5,'Vampire Academy','Fantasy')
    b6 = (6,'The Lost Hero','Fantasy')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mydb.commit()
    mycursor.execute("SELECT * FROM Fantasy")
    for db in mycursor:
        print(db)



# For Table Category Horror
    mycursor.execute("CREATE TABLE Horror(ID INT,BOOKNAME VARCHAR(255),CATEGORY VARCHAR(255))")
    query = "INSERT INTO Horror(ID,BOOKNAME,CATEGORY) VALUES(%s,%s,%s)"
    b1 = (1,'Dracula','Horror')
    b2 = (2,'The Tell-Tale Heart','Horror')
    b3 = (3,'I Am Legend','Horror')
    b4 = (4,'Minion','Horror')
    b5 = (5,'The Hunger','Horror')
    b6 = (6,'World War Z','Horror')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mycursor.execute(query,b3)
    mycursor.execute(query,b4)
    mycursor.execute(query,b5)
    mycursor.execute(query,b6)
    mydb.commit()
    mycursor.execute("SELECT * FROM Fantasy")
    for db in mycursor:
        print(db)

db_connection()