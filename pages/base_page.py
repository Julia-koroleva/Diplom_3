import sys 
sys.path.append('..')
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверка URL")
    def check_page_url(self):
        return self.driver.current_url
    
    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, self.driver.find_element(*source), self.driver.find_element(*target))

    @allure.step('Клик на элемент')
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()
        return element

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator, condition="visible", timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        if condition == "visible":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "clickable":
           return wait.until(EC.element_to_be_clickable(locator))
        elif condition == "invisible":
           return wait.until(EC.invisibility_of_element_located(locator))
        else:
            return wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Получить атрибут элемента')
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text
    
    @allure.step ('Обертка для выполнения JavaScript')
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    @allure.step ('Клик через JavaScript')
    def click_via_js(self, element):
        self.execute_script("arguments[0].click();", element)

    @allure.step ('Загрузка страницы')
    def load_page(self, page):
        WebDriverWait(self.driver, 15).until(
            EC.url_to_be(page)
        )