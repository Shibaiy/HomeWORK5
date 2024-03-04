import os
import time
import requests
import selene
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

os.mkdir('tmp')

browser.open("https://github.com/Shibaiy/HomeWORK/blob/main/Files/Xlsx-1.xlsx")
download_url = selene.browser.element('[data-testid="raw-button"]').get(selene.query.attribute("href"))
content = requests.get(url=download_url).content
with open("tmp/xlsx_test.xlsx", 'wb') as file:
    file.write(content)

browser.open("https://github.com/Shibaiy/HomeWORK/blob/main/Files/CSV-2.csv")
download_url = selene.browser.element('[data-testid="raw-button"]').get(selene.query.attribute("href"))
content = requests.get(url=download_url).content
with open("tmp/csv_test.csv", 'wb') as file:
    file.write(content)

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.getcwd() + r'\tmp'
}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
browser.config.driver = driver

browser.open("https://github.com/Shibaiy/HomeWORK/blob/main/Files/PDF-3.pdf")
browser.element('[data-testid="download-raw-button"]').click()
time.sleep(3)