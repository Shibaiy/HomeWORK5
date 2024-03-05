import  os
import time
import requests
import selene
import variables as v
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

os.mkdir('tmp')

def download_file(file_path):
    download_url = selene.browser.element('[data-testid="raw-button"]').get(selene.query.attribute("href"))
    content = requests.get(url=download_url).content
    with open(file_path, 'wb') as file:
        file.write(content)

browser.open(v.current_url + v.file_1)
download_file("tmp/xlsx_test.xlsx")

browser.open(v.current_url +v.file_2)
download_file("tmp/csv_test.csv")

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": v.download_default_directory
}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
browser.config.driver = driver

browser.open(v.current_url + v.file_3)
browser.element('[data-testid="download-raw-button"]').click()
time.sleep(3)
