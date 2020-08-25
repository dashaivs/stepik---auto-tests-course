from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который считает значение и вписывает его в поле
    sunduk = browser.find_element_by_id('treasure')
    x = sunduk.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #отмечаем checkbox
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    #отмечаем radiobutton
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

