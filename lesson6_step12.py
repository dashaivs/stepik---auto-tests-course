from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который считает значение и вписывает его в поле
    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    x1 = num1.text
    x2 = num2.text
    y = str(int(x1) + int(x2))
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y) # ищем элемент сщ значением "y"


    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

