from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bot:
    def __init__(self, username, password,hashtag):

        self.username = username
        self.password = password
        self.hashtag=hashtag
       
        self.driver = webdriver.Firefox()
        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        
        # Явное ожидание до появления поля для ввода имени пользователя
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )
        
        username_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Явное ожидание для перехода на следующую страницу после входа
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='button']"))
        )
        
        try:
            not_now_button = self.driver.find_element(By.CSS_SELECTOR, "div[role='button']")
            not_now_button.click()
            sleep(3)  # Время на выполнение действий после нажатия кнопки
        except Exception as e:
            print('The "Not Now" button was not found:', e)
        
        self.driver.get(f'https://www.instagram.com/explore/tags/ufc')

# Пример использования класса Bot
bot1 = Bot('murtazo__204', 'Murtazo$$08','')
