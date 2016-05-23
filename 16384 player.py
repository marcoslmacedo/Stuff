from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()

driver.get("http://annimon.github.io/16384/")

time.sleep(5)

body = driver.find_element_by_xpath("//div[@class='game-container']")

while True:
    body.send_keys(Keys.UP)
    body.send_keys(Keys.RIGHT)
    body.send_keys(Keys.DOWN)
    body.send_keys(Keys.LEFT)
