from fpdf import FPDF
import csv
import psycopg2

# creating a pdf 
def my_function(spacing=1):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica',size=20)
    pdf.cell(200,10,txt="Employe Table",ln = 2, align = "c")
    pdf.output("Table1.pdf")



    header = 'EMPLOY TABLE'
    data = [['id', 'Firstname','Last Name', 'Gender', 'Salary','DOB'],
            ['1', 'John', 'Cena', 'Male','25000','2000-01-02'],
            ['2', 'Randy', 'Orton', 'Male','10000','1998-06-05'],
            ['3', 'Tim', 'David', 'Male','5000','1999-12-12'],
            ['4','Ellyse','Perry','Female','12345','1990-09-23'],
            ['5','Sarah','Taylor','Female','9876','2001-01-12'],
            ['6','rahul','Dravid','Male','23500','1995-12-25'],
            ]
    
    pdf = FPDF()
    pdf.set_font("helvetica", size=12)
    pdf.add_page()
    
    col_width = pdf.w / 8.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)
        
    pdf.output('EmployData1.pdf')
    
if __name__ == '__main__':
    my_function()


# show the csv data into table format
def my_function1(query):
    
    conn = psycopg2.connect(
        host='localhost',
        user='postgres', 
        password = "root",
        database='postgres',
        )

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()

    with open('Delimeter1.csv','r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            if len(row) > 0:
                query =''' "INSERT INTO students(ID,Firstname,Lastname,Gender,Salary,DOB) 
                    VALUES({},'{}','{}','{}',{},'{}')".
                    format(row[0], row[1], row[2], row[3], row[4], row[5]) '''
                print(query)

            my_function1(query)

   

        
