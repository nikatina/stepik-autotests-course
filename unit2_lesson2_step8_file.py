from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys("Name")
    input_lname = browser.find_element_by_name("lastname")
    input_lname.send_keys("Lastname")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("email@ya.ru")

    file_btn = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_btn.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
