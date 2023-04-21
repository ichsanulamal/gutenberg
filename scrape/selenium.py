import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromrdriver = "/home/chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://medium.com/search?q=data%20science")

ScrollNumber = 50
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,50000)")
    time.sleep(5)

file = open('DS.html', 'w')
file.write(driver.page_source)
file.close()

driver.close()