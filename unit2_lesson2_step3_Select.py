from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum_num12 = int(num1) + int(num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_num12))  # ищем элемент с текстом "sum_num12"

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
