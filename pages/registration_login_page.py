import sys 
sys.path.append('..')
import allure
from data import *
from locators.locator_login_page import LoginPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from urls import * 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        WebDriverWait(self.driver, 15).until(
            EC.url_to_be(login_site)
        )


class Auth:
    @staticmethod
    def login_user(driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_entrance_button()
        login_page.load_login_page()
        login_page.login()
        
        return main_page
