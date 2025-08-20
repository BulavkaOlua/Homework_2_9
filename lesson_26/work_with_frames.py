from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:

    driver.get("http://localhost:8000/dz.html")

    driver.switch_to.frame("frame1")
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")

    button1 = driver.find_element(By.TAG_NAME, "button")
    button1.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert1 = driver.switch_to.alert
    assert alert1.text == "Верифікація пройшла успішно!"
    alert1.accept()

    driver.switch_to.default_content()


    driver.switch_to.frame("frame2")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")

    button2 = driver.find_element(By.TAG_NAME, "button")
    button2.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert2 = driver.switch_to.alert
    assert alert2.text == "Верифікація пройшла успішно!"
    alert2.accept()

finally:
    time.sleep(5)
    driver.quit()
