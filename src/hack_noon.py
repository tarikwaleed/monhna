from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email
import os


def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    return driver


def open_page(driver, url):
    driver.get(url)


def enter_email(driver, email):
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)
    except Exception as e:
        print("Error while entering email:", e)


def click_next_button(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "signInBtn"))
        )
        next_button = driver.find_element(by=By.CLASS_NAME, value="signInBtn")
        next_button.click()
    except Exception as e:
        print("Error while clicking Next button:", e)


def enter_otp(driver, otp):
    try:
        otp_inputs = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "sc-epptyN"))
        )

        for i in range(6):
            otp_inputs[i].send_keys(otp[i])
    except Exception as e:
        print("Error while entering OTP:", e)


def main():
    url = "https://login.noon.partners/en/?domain=https://ambassadors.noon.partners/en/coupons"
    # url="https://google.com"
    email = "Abdullah@monhna.com"

    email_password = os.getenv("EMAIL_PASSWORD")

    driver = initialize_driver()
    open_page(driver, url)
    enter_email(driver, email)
    click_next_button(driver)
    enter_otp(driver, otp="327791")
    click_next_button(driver)

    # otp = fetch_otp_from_email(email, email_password)

    # driver.quit()


if __name__ == "__main__":
    main()
