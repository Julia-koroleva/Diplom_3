import sys 
sys.path.append('..')
import allure
from data import *
from locators.locator_login_page import LoginPageLocators
from pages.base_page import BasePage
from urls import * 



class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод тестовых данных для аутентификации')
    def login(self):
        self.wait_for_element(LoginPageLocators.email_login).send_keys(Credantial.email)  
        self.wait_for_element(LoginPageLocators.password_login).send_keys(Credantial.password)  
        self.wait_for_element(LoginPageLocators.button_in).click()  
        
    @allure.step('Ожидание загрузки  страницы ввода логина и пароля')
    def load_login_page(self):
        self.load_page(login_site)
        

        
        