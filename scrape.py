from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='PATH_TO_WEBDRIVER')
urls = ['https://mcm.amazon.com/']

for url in urls:
    driver.get(url)
    print(driver.text())

driver.close()