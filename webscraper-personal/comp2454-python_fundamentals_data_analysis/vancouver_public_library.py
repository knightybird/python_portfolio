# import pandas as pd
# DRIVER_PATH        = "C:\\Users\\Owl\\Documents\\ChromeDriver\\chromedriver.exe"
# CSV_FILE    = 'grades.csv'
# dataset     = { "NumericGrade":[99,98,84], "LetterGrade":['A+', 'A', 'B']}
# dfOut       = pd.DataFrame( data = dataset)
#
# # Here I have decided to use a tab separator.
# # The default separator is a comma which also could work.
# dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep='\t')
#
# # Since I saved the file with a tab separator the instruction
# # that reads the content must also use a tab separator.
# dfIn        = pd.read_csv(DRIVER_PATH + CSV_FILE, sep='\t')
# print(dfIn.head(2))


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

DRIVER_PATH = "C:\\Users\\Owl\\Documents\\ChromeDriver\\chromedriver.exe"

URL = "https://www.rottentomatoes.com/critics/latest_reviews"
# URL = "https://vpl.bibliocommons.com/events/search/index"
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

content = browser.find_elements_by_css_selector(".event-row")

for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    print(rawString)
    print("***")
    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    location = eventArray[len(eventArray) - 1]
    print("Name:     " + eventName)
    print("Date:     " + eventDate)
    print("Time:     " + eventTime)
    print("Location: " + location)
    print("***")


time.sleep(4)
button = browser.find_element_by_css_selector(".btn-lg")
for i in range(0,20):
    button.click()
    '''
    If you see the following error increase the sleep time:
    ElementClickInterceptedException: element click intercepted:
    '''
    print("Count: ", str(i))
    time.sleep(4)
print("done loop")


