import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def take_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


class NovaPoshtaTrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Відкрити сторінку відстеження Нової Пошти")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Ввести номер ТТН: {ttn}")
    def enter_ttn(self, ttn: str):
        input_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#en"))
        )
        input_field.clear()
        input_field.send_keys(ttn)
        # натискаємо кнопку пошуку
        search_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#np-number-input-desktop-btn-search-en"))
        )
        search_btn.click()

    @allure.step("Отримати статус доставки")
    def get_status(self) -> str:
        status_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#chat > header > div.header__parcel-dynamic-status.px-4.d-flex.align-center > div.flex-grow-1 > div.header__status-text"))
        )
        return status_element.text.strip()

    @allure.step("Отримати повідомлення про помилку")
    def get_error_message(self) -> str:
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#np-number-input-desktop-message-error-message > span"))
        )
        return error_element.text.strip()

    @allure.step("Перевірити наявність логотипу")
    def is_logo_displayed(self) -> bool:
        logo = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#np-main-desktop-link-logo > div > div.v-responsive__sizer"))
        )
        return logo.is_displayed()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ Тест 1 — валідний ТТН
@allure.feature("Відстеження відправлень Нова Пошта")
def test_valid_tracking_number(driver):
    ttn = "20400443306434"  # заміни на справжній робочий ТТН
    expected_status = "Отримана"

    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.enter_ttn(ttn)

    status = page.get_status()
    take_screenshot(driver, "Статус доставки")

    assert expected_status in status, f"Очікувалось '{expected_status}', а отримали '{status}'"


# ✅ Тест 2 — невалідний ТТН
@allure.feature("Відстеження відправлень Нова Пошта")
def test_invalid_tracking_number(driver):
    invalid_ttn = "00000000000000"

    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.enter_ttn(invalid_ttn)

    error_msg = page.get_error_message()
    take_screenshot(driver, "Помилка для невалідного ТТН")

    assert "не знайдено" in error_msg.lower() or "невірний" in error_msg.lower(), \
        f"Очікувалось повідомлення про помилку, а отримали '{error_msg}'"


# ✅ Тест 3 — наявність логотипу
@allure.feature("Елементи сторінки")
def test_logo_presence(driver):
    page = NovaPoshtaTrackingPage(driver)
    page.open()

    assert page.is_logo_displayed(), "Логотип Нової Пошти не відображається"
    take_screenshot(driver, "Логотип сайту")


# ✅ Тест 4 — наявність поля вводу
@allure.feature("Елементи сторінки")
def test_input_field_presence(driver):
    page = NovaPoshtaTrackingPage(driver)
    page.open()

    input_field = driver.find_element(By.CSS_SELECTOR, "#en")
    take_screenshot(driver, "Поле вводу ТТН")

    assert input_field.is_displayed(), "Поле вводу ТТН не відображається"


# ✅ Тест 5 — наявність кнопки пошуку
@allure.feature("Елементи сторінки")
def test_search_button_presence(driver):
    page = NovaPoshtaTrackingPage(driver)
    page.open()

    search_btn = driver.find_element(By.CSS_SELECTOR, "#np-number-input-desktop-btn-search-en")
    take_screenshot(driver, "Кнопка пошуку")

    assert search_btn.is_displayed(), "Кнопка пошуку не відображається"
