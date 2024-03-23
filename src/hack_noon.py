import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from gmail_access import get_otp


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


def click_button(driver, class_name):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        button = driver.find_element(by=By.CLASS_NAME, value=class_name)
        button.click()
    except Exception as e:
        print("Error while clicking Next button:", e)


def enter_otp_v1(driver, class_name, otp):
    try:
        otp_inputs = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "sc-epptyN"))
        )

        for i in range(6):
            otp_inputs[i].send_keys(otp[i])
    except Exception as e:
        print("Error while entering OTP:", e)


def enter_otp_v2(driver, otp):
    try:
        otp_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "emailOtp"))
        )
        otp_input.send_keys(otp)

    except Exception as e:
        print("Error while entering OTP:", e)


def enter_copoun_details(driver, coupon_prefix, coupon_count):
    class_name = "styles_input__sR5Gb"

    try:
        inputs = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        if inputs:
            inputs[2].send_keys(coupon_prefix)
            inputs[3].send_keys(coupon_count)
        else:
            print(f"No inputs found with class name: {class_name}")
    except Exception as e:
        print("can not locate copun details inputs", e)


def click_button_of_multiple(driver, index, class_name="styles_button__VMIgL"):
    try:
        buttons = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        print(f"buttons are:\n{buttons}")
        if buttons:
            buttons[index].click()  # Click the first button
        else:
            print("No buttons found with class name:", class_name)
    except Exception as e:
        print("Error while clicking button:", e)


def main():
    url_v1 = "https://login.noon.partners/en/?domain=https://ambassadors.noon.partners/en/coupons"
    url_v2 = "https://ambassadors.noon.partners/en/coupons?project=PRJ65632"

    email = "Abdullah@monhna.com"

    next_button_class_name = "signInBtn"
    continue_button_class_name = "sc-2acab29e-0"
    opt_input_class_name_v2 = "emailOtp"

    driver = initialize_driver()
    open_page(driver, url_v2)
    enter_email(driver, email)
    click_button(driver, class_name=continue_button_class_name)
    time.sleep(6)
    otp = get_otp()
    enter_otp_v2(driver=driver, otp=otp)
    click_button(driver, class_name=continue_button_class_name)
    click_button_of_multiple(driver=driver, index=0)
    enter_copoun_details(driver, "TARIK", 10)
    time.sleep(1)
    click_button_of_multiple(driver=driver, index=5)
    # click_create_copoun_button(driver)
    # driver.quit()


if __name__ == "__main__":
    main()
