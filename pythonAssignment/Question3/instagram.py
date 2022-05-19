from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget
import csv
import pymysql

def func():
    driver =webdriver.Chrome('/home/neosoft/Documents/chromedriver_linux64/chromedriver')
    driver.get("https://www.instagram.com/")
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

    username.clear()
    password.clear()
    username.send_keys("shekason_tanzil")
    password.send_keys("******")
    log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not now')]"))).click()
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()

    searchbox = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    searchbox.clear()
    keyword = "#cat"
    searchbox.send_keys(keyword)

    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)

    driver.execute_script("window.scrollTo(0,25);")
    images = driver.find_elements_by_tag_name('img')
    images = [image.get_attribute('src') for image in images]
    print(images)

    lines = []
    with open('img.csv', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

    x = open("img.csv",'a')
    print(images,file = x)
    x.close()

func()

filename = "img.csv"
def db_connection(query):

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="tanzil12345",
        db='user'
    )

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()


with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in fields:
        if len(row) > 0:
            query = "INSERT INTO instagram(Links) values(" + row + ");"
            print(query)
            
            db_connection(query)
