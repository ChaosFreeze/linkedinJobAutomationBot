import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Filter the job search and select Easy Apply
# Then copy the URL and store it in JOB_LINK
JOB_LINK = 'YOUR_LINKEDIN_URL_WITH_ALL_FILTERS'
EMAIL = "YOUR_EMAIL_ID"
PASSWORD = "YOUR_PASSWORD"
PHONE_NUMBER = "YOUR_PHONE_NUMBER"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(JOB_LINK)

# Sign in
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
# time.sleep(30)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(EMAIL)
time.sleep(30)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
sign_in = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in.click()
time.sleep(10)

# # apply for a single job
# apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
# apply_button.click()
# time.sleep(10)
# phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE_NUMBER)
# # submit the application
# submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
# submit_button.click()

# apply for many jobs
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)
        # submit the application
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue-unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Complex Application. Skipped.")
            continue
        else:
            submit_button.click()
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No Application button Skipped.")
        continue

# Logout of LinkdeIn
profile_pic_button = driver.find_element(By.CSS_SELECTOR, ".global-nav__me button")
profile_pic_button.click()

time.sleep(3)
sign_out_button = driver.find_element(By.XPATH, '//*[@id="ember19"]/div/ul/li[3]/a')
# couldn't do it by click() method, so used ENTER
sign_out_button.send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()
