import pytest
import allure
from selenium import webdriver
from urls import *
from data import *
from selenium import webdriver
from pages.registration_login_page import LoginPage
from locators.locator_main_page import MainPageLocators
from urls import *


@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    if request.param == "Firefox":
        driver = webdriver.Firefox()
    elif request.param == "Chrome":
        driver = webdriver.Chrome()
    driver.get(main_site)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(login_site)
    login_page = LoginPage(driver)
    login_page.load_login_page()
    login_page.login()
    login_page.wait_for_element(MainPageLocators.busket)
    return driver