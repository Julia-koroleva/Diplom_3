import sys 
sys.path.append('..')
import allure
from locators.locator_main_page import MainPageLocators
from .base_page import BasePage
from urls import *

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на кнопку "Конструктор" в хедере страницы')
    def click_button_constructor(self):
        self.click_element(MainPageLocators.constructor)
        

    @allure.step('Клик по кнопке Войти в эккаунт')
    def click_entrance_button(self):
        self.click_element(MainPageLocators.entrance_button)
     
    
    @allure.step('Клик по кнопке "Лента заказов" в хедере страницы')
    def click_list_of_orders(self):
        self.click_element(MainPageLocators.list_of_orders)

    @allure.step('Поиск элемента на всплывающем окне "Детали ингредиента"')
    def find_element_on_ingredient_window(self):
        element = self.wait_for_element(MainPageLocators.ingredient_details)
        return element

    @allure.step('Клик по Ингредиенту')
    def click_ingredient(self):
        element = self.click_element(MainPageLocators.ingredient)
        return element

    @allure.step('Клик по крестику на странице деталей Ингредиента')
    def click_cross_ingredient(self):
        element = self.click_element(MainPageLocators.cross_click)
        return element

    @allure.step('Клик по счетчику ингредиента')
    def get_counter_value(self):
        self.wait_for_element(MainPageLocators.counter_ingredient)
        counter = self.get_element_text(MainPageLocators.counter_ingredient)
        return counter

    @allure.step('Проверка нахождения на главной странице')
    def check_main_page(self):
        return self.check_page_url() == main_site
    
    @allure.step('Проверка нахождения на странице Лента заказов')
    def check_order_page(self):
        return self.check_page_url() == order_site
        
    @allure.step('Добавить Ингредиент в бургер')
    def add_ingredient(self):
       self.wait_for_element(MainPageLocators.ingredient)
       self.drag_and_drop_element(MainPageLocators.ingredient, MainPageLocators.busket)
       self.wait_for_element(MainPageLocators.counter_ingredient)

    @allure.step('Оформить заказ')
    def make_order(self):
        self.add_ingredient()
        self.click_element(MainPageLocators.make_order)
    
    @allure.step('Ожидание загрузки  модального окна энгредиента')
    def wait_for_ingredient_modal(self):
        element = self.wait_for_element(MainPageLocators.cross_click)
        return element
      

        
    

    





    