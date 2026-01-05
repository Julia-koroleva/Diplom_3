import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class LoginPageLocators:
   # Поле для ввода адреса электронной почты на странице ввода логина и пароля
    email_login =  (By.XPATH, '//input[@type="text"]') 

   # Поле для ввода пароля на странице ввода логина и пароля
    password_login = (By.XPATH, '//input[@type="password"]')

    # Кнопка "Войти" на странице ввода логина и пароля
    button_in = (By.XPATH, '//button[contains(@class, "button_button_type_primary")]')
   
   
