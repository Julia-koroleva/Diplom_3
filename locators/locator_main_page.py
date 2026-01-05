import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Конструктор"
    constructor = (By.XPATH, '//a[contains(@class, "AppHeader_header__link") and @href = "/"]')
    # Кнопка "Лента заказов"
    list_of_orders = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(text(), 'Лента')]")
    # Ингредиент 
    ingredient = (By.XPATH, "//img[contains(@class, 'BurgerIngredient_ingredient__image')]")
    # Клик по крестику
    cross_click = (By.XPATH, '//h2[contains(@class,"text_type_main-large")]/parent::div/parent::div/button[contains(@class, "close")]')
    # Счетчик ингредиентов
    counter_ingredient = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    # Кнопка "Войти в эккаунт" на главной странице
    entrance_button = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    # Кнопка оформить заказ
    make_order = (By.XPATH,  "//button[contains(text(), 'Оформить заказ')]")
    # Кнопка булки
    buns = (By.XPATH, "//span[text()='Булки']/..")
    # Детали ингредиента
    ingredient_details = (By.XPATH, '//h2[contains(@class,"text_type_main-large")]')
    # Корзина перетаскивания ингредиента
    busket = (By.XPATH, "//ul[@class=\"BurgerConstructor_basket__list__l9dp_\"]/parent::section")
  
    










    