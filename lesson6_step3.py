from selenium import webdriver
import time
import math 


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("img")
    
    x = input1.get_attribute("valuex")
    y = calc(x)
    
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    
    input3 = browser.find_element_by_id("robotCheckbox")
    input3.click()
    
    input4 = browser.find_element_by_id("robotsRule")
    input4.click()

    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    time.sleep(10)
    # успеваем скопировать код за 30 секунд
    # закрываем браузер после всех манипуляций
    browser.quit()

