import os
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    with open('test.txt', 'w') as file:
       file.write('01010100101')
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    file_path = os.path.join(current_dir, 'test.txt')
    loader = browser.find_element_by_css_selector('[type="file"]') 
    loader.send_keys(file_path)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk")
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
