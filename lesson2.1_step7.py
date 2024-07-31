from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import math

link = "http://suninjuly.github.io/get_attribute.html"

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)

    # Найти элемент-картинку и получить значение атрибута valuex
    treasure_image = browser.find_element(By.ID, "treasure")
    x_value = treasure_image.get_attribute("valuex")
    y = calc(x_value)

    # Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отметить checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # Нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ожидание перед закрытием браузера
    time.sleep(10)
    browser.quit()
