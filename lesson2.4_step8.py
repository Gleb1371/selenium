from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/explicit_wait2.html"

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)

    # Ожидание, когда цена станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решение математической задачи
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажатие на кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Ожидание перед закрытием браузера
    time.sleep(10)
    browser.quit()
