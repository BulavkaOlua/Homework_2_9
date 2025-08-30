import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.pages.registration_page import RegistrationPage


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()


@pytest.fixture
def open_registration_form(driver):
    """Відкриває форму реєстрації"""
    driver.find_element(*RegistrationPage.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(RegistrationPage.REGISTRATION_BUTTON)
    )
    driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()


@pytest.fixture
def fill_registration_form(driver):
    """Заповнює форму реєстрації"""
    def _fill(first, last, email, password):
        driver.find_element(*RegistrationPage.FIRST_NAME).send_keys(first)
        driver.find_element(*RegistrationPage.LAST_NAME).send_keys(last)
        driver.find_element(*RegistrationPage.EMAIL).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationPage.REPASSWORD).send_keys(password)
    return _fill


@pytest.fixture
def submit_registration(driver):
    """Натискає кнопку Register"""
    def _submit():
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    return _submit


@pytest.fixture
def wait_for_success(driver):
    """Очікує повідомлення про успішну реєстрацію"""
    def _wait():
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPage.SUCCESS_ALERT)
        )
        return driver.find_element(*RegistrationPage.SUCCESS_ALERT).text
    return _wait


@pytest.fixture
def generate_email():
    """Генерує унікальний email для тесту"""
    timestamp = int(time.time())
    rand = random.randint(100, 999)
    return f"test_{timestamp}_{rand}@example.com"
