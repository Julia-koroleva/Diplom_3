import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Общее количество выполненных заказов за все время
    total_order_list = (By.XPATH, '//p[contains(text(), "за все время")]/parent::div/p[contains(@class, "text_type_digits")]')
    # Кнопка закрытия заказа
    order_close_button = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") 
    # Оверлей
    overlay = (By.XPATH, '//img[contains(@class, "loading")]/parent::div')
    # Выполнено заказов за сегодня
    order_made_today = (By.XPATH, '//p[contains(text(), "за сегодня")]/parent::div/p[contains(@class, "text_type_digits")]')
    # Номер оформленного заказа
    your_order = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    # Модальное окно
    modal_window = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")   

    @staticmethod
    def order_in_progress(order_number):
        links = f'//ul[contains(@class,"orderListReady")]/li[contains(text()[2], "{order_number}")]'
        locator = (By.XPATH, links)
        return locator
