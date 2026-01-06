import sys 
sys.path.append('..')
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from urls import *
from Diplom_3.conftest import *


class TestOrderPage:
    @allure.title('Проверка  увеличения счётчика «Выполнено за всё время» при создании нового заказа')
    @allure.description('Счетчик «Выполнено за всё время» увеличится если создать новый заказ')
    def test_check_count_list_of_orders(self, driver, login):
        main_page = MainPage(login) 
        order_page = OrderPage(driver)
        order_page.wait_overlay_hidden()
        main_page.click_list_of_orders()
        total_1 = order_page.get_total_list_counter()
        main_page.click_button_constructor()
        main_page.make_order()
        order_page.wait_overlay_hidden()
        order_page.click_cross_order()
        order_page.wait_window_hidden()
        main_page.click_list_of_orders()
        total_2 = order_page.get_total_list_counter()
        assert total_2 > total_1 

    @allure.title('Проверка  увеличения счётчика «Выполнено за сегодня" при создании нового заказа')
    @allure.description('Счетчик «Выполнено за сегодня» увеличится если создать новый заказ')
    def test_check_count_list_of_orders_today_success(self, driver, login):
        main_page = MainPage(login) 
        order_page = OrderPage(driver)
        order_page.wait_overlay_hidden()
        main_page.click_list_of_orders()
        today_1 = order_page.get_today_order_counter()
        main_page.click_button_constructor()
        main_page.make_order()
        order_page.wait_overlay_hidden()
        order_page.click_cross_order()
        order_page.wait_window_hidden()
        main_page.click_list_of_orders()
        today_2 = order_page.get_today_order_counter()
        assert  int(today_2) > int(today_1)
   

    @allure.title('Проверка появление нового заказа в ленте заказов в работе')
    @allure.description('Новый заказ после создания появляется в перечне заказов в работе')
    def test_check_count_list_of_orders_in_process_success(self, driver, login):
        main_page = MainPage(login) 
        order_page = OrderPage(driver)
        order_page.wait_overlay_hidden()
        main_page.make_order()
        order_page.wait_overlay_hidden()
        order_number = order_page.get_your_order()
        order_page.click_cross_order()
        order_page.wait_window_hidden()
        main_page.click_list_of_orders()
        order_page.wait_overlay_hidden()
        assert order_page.check_order_in_progress(order_number) 