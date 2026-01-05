import sys 
sys.path.append('..')
import allure
from locators.locator_order_page import OrderPageLocators
from .base_page import BasePage
from urls import *
from selenium.common.exceptions import ElementClickInterceptedException

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
     
    @allure.step('Дождаться закрытия окна')
    def wait_window_hidden(self):
        self.wait_for_element(OrderPageLocators.modal_window, "invisible")
        return True

    @allure.step('Дождаться закрытия окна на странице заказа')
    def wait_overlay_hidden(self):
        self.wait_for_element(OrderPageLocators.overlay, "invisible")

    @allure.step('Проверяем что заказ в работе')
    def check_order_in_progress(self, order_number):
        self.wait_for_element(OrderPageLocators.order_in_progress(order_number))
        return self.get_element_text(OrderPageLocators.order_in_progress(order_number))
    
    @allure.step('Получение списка заказов "Выполнено за все время')
    def get_total_list_counter(self):
        self.wait_for_element(OrderPageLocators.total_order_list)
        counter = self.get_element_text(OrderPageLocators.total_order_list)
        return counter
    
    @allure.step('Клик по крестику на странице деталей Заказа')
    def click_cross_order(self):
        element = self.wait_for_element(OrderPageLocators.order_close_button, "clickable")
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
            self.wait_window_hidden()

    @allure.step('Получение списка заказов "Выполнено за сегодня"')
    def get_today_order_counter(self):
        self.wait_for_element(OrderPageLocators.order_made_today)
        counter = self.get_element_text(OrderPageLocators.order_made_today)
        return counter
    
    @allure.step('Получение списка твоего заказа')
    def get_your_order(self):
        self.wait_for_element(OrderPageLocators.your_order)
        counter = self.get_element_text(OrderPageLocators.your_order)
        return counter
    

        
