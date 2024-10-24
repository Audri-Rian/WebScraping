from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sqlite3


def create_database():
    conn = sqlite3.connect('flipkart_products.db')
    c = conn.cursor()
    c.execute ('''CREATE TABLE IF NOT EXISTS products
               (id INTERGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               price TEXT,
               rating TEXT,
               desc TEXT,
               img_url)''')
    conn.commit()
    conn.close()

def scrape_flipkart(url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
    driver.get(url)

    products = driver.find_element(By.CLASS_NAME, 'CGtC98')