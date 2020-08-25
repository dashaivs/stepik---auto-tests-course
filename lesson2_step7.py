from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена уменьшится до 100
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button.click()

#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x_element = browser.find_element_by_id('input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

# Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
