from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

link = "https://suninjuly.github.io/selects1.html"

try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)

    # Найти элементы, содержащие числа
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # Посчитать сумму чисел
    sum_result = num1 + num2

    # Выбрать значение из выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_result))

    # Нажать на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ожидание перед закрытием браузера
    time.sleep(10)
    browser.quit()
