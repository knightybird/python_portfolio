import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

DRIVER_PATH = "C:\\Users\\Owl\\Documents\\ChromeDriver\\chromedriver.exe"

URL = "https://www.bcit.ca/programs/applied-data-analytics-certificate-part-time-5512cert/#courses"
browser = None

# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(DRIVER_PATH)
    print("The path to webdriver_manager was found.")

# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'DRIVER_PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

content = browser.find_elements_by_css_selector(".course_name")
size = len(content)
print(size)
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="lxml")
    print(soup.get_text())
    print("***")  # Go to new line.
