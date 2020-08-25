from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.form-group input[name = firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.form-group input[name = lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.form-group input[name = email]")
    input3.send_keys("gobalticdasha@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

