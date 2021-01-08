from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.recreation.gov/camping/campgrounds/233626/availability')

search = browser.find_element_by_id("campsite-filter-search")
search.send_keys("Pcam")
search.send_keys(Keys.RETURN)

date = browser.find_element_by_id("single-date-picker-1")
date.click()
arrow = browser.find_element_by_class_name('sarsa-icon rec-icon-arrow-forward md')
arrow.click()

time.sleep(10)

browser.quit()
