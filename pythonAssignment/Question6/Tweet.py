import tweepy
import pymysql
import textwrap
from fpdf import FPDF

def function():
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAPbVcAEAAAAAhYb%2By%2F1NA40VX6K4GUc%2BK0ZtkOk%3DPHwBLHShnQhsFEoxmN6NH6yPG914LaPWPegLzibNHQkI70YIwJ')

    query = 'from:suhemparack -is:retweet'

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

    for tweet in tweets.data:
        print(tweet.text)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)


    list = []
    for result in tweet.context_annotations:
        result = tweet.context_annotations
        list.append(result)
        print(list)

        lines = list
        with open('readme.txt', 'w') as f:
            for line in lines:
                f.write(str(list))
                f.write('\n')

function()

def db_connection(query):
    mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "tanzil12345",
        db = "mysql"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tweets2(Id INT,Name Varchar(255),Description VARCHAR(255),entity_id INT,entity_name VARCHAR(255))")
    query = "INSERT INTO tweets1(Id,Name,Description,entity_id,entity_name) VALUES(%s,%s,%s,%s,%s)"
    b1 = (46,'Brand Category','Categories within Brand Verticals',78,'Services')
    b2 = (47,'Brand','Brand and companies',10,'Twitter')
    mycursor.execute(query,b1)
    mycursor.execute(query,b2)
    mydb.commit()
    

    db_connection(query)



def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')

    input_filename = 'readme.txt'
    output_filename = 'tweets.pdf'
    file = open(input_filename)
    text = file.read()
    file.close()
    text_to_pdf(text, output_filename)


