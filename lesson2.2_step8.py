from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/file_input.html"

try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)

    # Явное ожидание элементов
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    )

    # Заполнение формы
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email@example.com")
    
    # Подготовка файла для загрузки
    file_name = "file.txt"
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'w') as file:
        file.write("")  # создаем пустой файл
    
    # Загрузка файла
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Поиск кнопки с текстом 'Submit' и клик по ней
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ожидание перед закрытием браузера
    time.sleep(10)
    browser.quit()
    # Удаление файла после использования
    os.remove(file_path)
