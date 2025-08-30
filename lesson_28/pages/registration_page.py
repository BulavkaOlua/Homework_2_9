
from selenium.webdriver.common.by import By


class RegistrationPage:
    # 🔹 кнопка "Sign In" (у хедері)
    SIGN_IN_BUTTON = (
        By.CSS_SELECTOR,
        "body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_right.d-flex.align-items-center > button.btn.btn-outline-white.header_signin"
    )

    # 🔹 кнопка "Registration" у модальному вікні логіну
    REGISTRATION_BUTTON = (
        By.XPATH,
        "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]"
    )

    # 🔹 поля форми реєстрації
    FIRST_NAME = (By.XPATH, '//*[@id="signupName"]')
    LAST_NAME = (By.XPATH, '//*[@id="signupLastName"]')
    EMAIL = (By.XPATH, '//*[@id="signupEmail"]')
    PASSWORD = (By.XPATH, '//*[@id="signupPassword"]')
    REPASSWORD = (By.XPATH, '//*[@id="signupRepeatPassword"]')

    # 🔹 кнопка підтвердження реєстрації
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Register']")

