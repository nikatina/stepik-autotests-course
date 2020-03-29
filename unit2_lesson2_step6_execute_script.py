from selenium import webdriver
import time
from math import *


def calc(x):
    return str(log(abs(12*sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value_x = browser.find_element_by_id("input_value")
    y = calc(value_x.text)

    browser.execute_script("window.scrollBy(0, 100);")
    input_form = browser.find_element_by_id("answer")
    input_form.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
