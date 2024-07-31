from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    # Найти значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Поиск кнопки с текстом 'Submit' и клик по ней
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ожидание перед закрытием браузера
    time.sleep(10)
    browser.quit()
