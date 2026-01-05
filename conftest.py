import pytest
import allure
from selenium import webdriver
from urls import *
from data import *
from selenium import webdriver


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


