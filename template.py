import time
from selenium import webdriver

driver = webdriver.Chrome('conf/chromedriver')
driver.get('http://www.google.com/')
# Let the user actually see something!
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
# Let the user actually see something!
time.sleep(5)
driver.quit()