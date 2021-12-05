from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/c/Sinvicta/videos")

driver.find_element_by_xpath('//*[@id="video-title"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="button"]').click()

