import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class NovaPoshtaTrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_ttn(self, ttn: str):
        input_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "en"))
        )
        input_field.clear()
        input_field.send_keys(ttn)
        input_field.send_keys(Keys.RETURN)

    def get_status(self) -> str:
        status_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
        )
        return status_element.text.strip()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_nova_poshta_tracking(driver):
    ttn = "20400443306434"
    expected_status = "Отримана"

    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.enter_ttn(ttn)
    status = page.get_status()

    assert status == expected_status, f"Очікувалось '{expected_status}', а отримали '{status}'"
