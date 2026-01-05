import sys 
sys.path.append('..')
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.registration_login_page import Auth
from urls import *
from Diplom_3.conftest import *

class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор')
    @allure.description('Проверка корректности перехода в раздел "Конструктор" по клику на "Конструктор"')
    def test_constructor_success(self, driver):
        main_page = Auth.login_user(driver) 
        order_page = OrderPage(driver)
        order_page.wait_overlay_hidden()
        main_page.click_list_of_orders()
        main_page.click_button_constructor()
        assert main_page.check_main_page()


    @allure.title('Проверка перехода по клику на страницу "Лента заказов"')
    @allure.description('Проверка корректности перехода на страницу "Лента заказов" по клику на "Лента заказов"')
    def test_list_of_orders_success(self, driver):
        main_page = Auth.login_user(driver) 
        order_page = OrderPage(driver)
        order_page.wait_overlay_hidden()
        main_page.click_list_of_orders()
        assert main_page.check_order_page()


    @allure.title('Проверка, что по клику на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Проверка успешного появления всплывающего окна с деталями при клике на ингредиент')
    def test_click_on_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.wait_for_ingredient_modal()
        assert main_page.find_element_on_ingredient_window()

    @allure.title('Проверка закрытия окна с деталями ингредиентапри клике на крестик')
    @allure.description('Проверка успешного закрытия окна с деталями ингредиентапри клике на крестик')
    def test_click_on_cross_ingredient_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_ingredient()
        main_page.wait_for_ingredient_modal()
        main_page.click_cross_ingredient()
        assert order_page.wait_window_hidden()

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('Проверка работы счетчика при добавлении ингредиента в заказ')
    def test_counter_success(self, driver):
        main_page = MainPage(driver)
        initial_count = main_page.get_counter_value()
        main_page.add_ingredient()
        new_count = main_page.get_counter_value()
        assert int(new_count) > int(initial_count)
   

   