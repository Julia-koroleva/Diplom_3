import pytest
import allure
from selenium import webdriver
from urls import *
from data import *
from pages.registration_login_page import *
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.registration_login_page import LoginPage

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


