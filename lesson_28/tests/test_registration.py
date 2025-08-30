import pytest
from selenium.webdriver.support.ui import WebDriverWait
from lesson_28.pages.registration_page import RegistrationPage
from datetime import datetime


def test_user_can_register(driver):
    driver.get("https://qauto2.forstudy.space/")

    # 🔹 відкриваємо модальне вікно входу
    driver.find_element(*RegistrationPage.SIGN_IN_BUTTON).click()
    driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()

    # 🔹 генеруємо унікальний email
    unique_email = f"olga_{datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"

    # 🔹 заповнюємо форму реєстрації
    driver.find_element(*RegistrationPage.FIRST_NAME).send_keys("Olga")
    driver.find_element(*RegistrationPage.LAST_NAME).send_keys("Test")
    driver.find_element(*RegistrationPage.EMAIL).send_keys(unique_email)
    driver.find_element(*RegistrationPage.PASSWORD).send_keys("Qwerty123!")
    driver.find_element(*RegistrationPage.REPASSWORD).send_keys("Qwerty123!")

    # 🔹 натискаємо кнопку реєстрації
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

    # 🔹 чекаємо, поки відкриється сторінка garage
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url == "https://qauto2.forstudy.space/panel/garage"
    )

    # 🔹 перевірка
    assert driver.current_url == "https://qauto2.forstudy.space/panel/garage"
