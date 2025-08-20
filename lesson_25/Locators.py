from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://qauto2.forstudy.space/")

time.sleep(2)

login_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

login_input.send_keys("guest")
password_input.send_keys("welcome2qauto")
login_button.click()

time.sleep(3)

class_locators = {
    "sign_in_button": "header_signin",
    "guest_login_button": "header-link",
    "instructions_img": "about-picture_img",
    "sign_up_button": "hero-descriptor_btn",
    "ithillel_link": "contacts_link",
}

partial_link_text_locators = {
    "ithillel_link": "ithillel",  # частина тексту посилання
    "home_link": "Hom",            # частина тексту посилання
}

name_locators = {
    "login_input": "email",        # поле логіну
    "password_input": "password",  # поле паролю
}

css_locators = {
    "sign_in_button": "button.header_signin",
    "guest_login_button": "button.header-link.-guest",
    "instructions_img": "div.about-picture img.about-picture_img[alt='Instructions']",
    "sign_up_button": "button.hero-descriptor_btn.btn-primary",
    "home_link": "a.header-link[href='/']",
    "about_button": "button.header-link[appscrollto='aboutSection']",
    "contacts_button": "button.header-link[appscrollto='contactsSection']",
    "play_button": "button.ytp-large-play-button",
    "ithillel_link": "a.contacts_link.display-4[href='https://ithillel.ua']",
}

xpath_locators = {
    "sign_in_button": "//button[text()='Sign In']",
    "guest_login_button": "//button[contains(text(),'Guest log in')]",
    "instructions_img": "//img[@alt='Instructions']",
    "sign_up_button": "//button[text()='Sign up']",
    "home_link": "//a[text()='Home']",
    "about_button": "//button[text()='About']",
}

link_text_locators = {
    "ithillel_link": "ithillel.ua",
    "home_link": "Home",  # якщо потрібно клікати по Home як посиланню
}

id_locators = {
    "about_section": "aboutSection",
    "contacts_section": "contactsSection",
}
