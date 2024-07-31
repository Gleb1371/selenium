from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import math

# Ссылка на сайт
link = "http://suninjuly.github.io/find_link_text"

try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)
    
    # Вычисление зашифрованного текста ссылки
    encoded_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    
    # Поиск ссылки по зашифрованному тексту и клик по ней
    link_element = browser.find_element(By.LINK_TEXT, encoded_text)
    link_element.click()
    
    # Заполнение формы
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Имя")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Фамилия")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Город")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Страна")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ждем, чтобы успеть скопировать код
    time.sleep(10)
    browser.quit()
