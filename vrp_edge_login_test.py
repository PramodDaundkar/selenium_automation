import datetime
import random

import time
from asyncio.log import logger

from _pytest import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# driver_path = "E:\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(driver_path)
# chrome_option = Options()
# chrome_option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(driver_path, chromeOption=chrome_option)

email_address = "pdaundkar9+" + datetime.datetime.now().strftime("%y%m%d%H%M") + "@gmail.com"
password = "Test@123"
print(email_address)
sign_up_url = 'https://together4healthva-vrp-edge.qak8s.vibrenthealth.com/'
login_url = 'https://together4healthva-vrp-edge.qak8s.vibrenthealth.com/login'


def test_complete_signup():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(sign_up_url)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "email").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.NAME, "verification_code")
    time.sleep(5)

    WebDriverWait(chrome_driver, 50).until(EC.element_to_be_clickable((By.ID, "action-button"))
                                           )
    chrome_driver.find_element(By.ID, "action-button").click()
    # driver.switch_to.alert.accept()
    WebDriverWait(chrome_driver, 50).until(
        EC.element_to_be_clickable((By.ID, "beginYourJournyContinueButton"))
    )
    chrome_driver.find_element(By.ID, "beginYourJournyContinueButton").click()
    print(chrome_driver.find_element(By.XPATH, "//span[@class = 'container-header']/span").text)
    assert chrome_driver.title == 'Dashboard'
    chrome_driver.find_element(By.XPATH, "//button[@title = 'Start']").click()
    time.sleep(20)

    WebDriverWait(chrome_driver, 50).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-target='@form|button|continue']")))
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()
    for i in range(17):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'Print Name of Participant']").send_keys("Pramod")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'Type Signature']").send_keys("Pramod")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()
    time.sleep(10)
    chrome_driver.find_element(By.XPATH, "//nav[@class='navigation-container']/ul/li[6]").click()
    chrome_driver.find_element(By.XPATH, "//a[@aria-label='Add Shipping Address']").click()
    chrome_driver.find_element(By.ID, "streetOne").send_keys("6644 E Baywood Ave")
    chrome_driver.find_element(By.ID, "city").send_keys("Mesa")
    sel_state = Select(chrome_driver.find_element(By.ID, "states"))
    sel_state.select_by_visible_text("Arizona")
    chrome_driver.find_element(By.ID, "zip").send_keys("85206")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='addressInfo.verification.next']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='addessInfo.verification.save']").click()
    time.sleep(20)
    chrome_driver.find_element(By.XPATH, "//nav[@class='navigation-container']/ul/li[1]").click()
    time.sleep(20)

    print("About You Form Started")
    chrome_driver.find_element(By.XPATH, "//button[@title = 'Start']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()
    chrome_driver.find_element(By.XPATH, "//input[@aria-label='First Name']").send_keys("Pramod")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label='Last Name']").send_keys("Daundkar")
    chrome_driver.find_element(By.XPATH, "//input[@placeholder='MM/DD/YYYY']").send_keys("01/01/2000")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH, "//input[@aria-label='Address line 1']").send_keys("6644 E Baywood Ave")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label='City']").send_keys("Mesa")
    sel_state = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'participant_address_state']"))
    sel_state.select_by_visible_text("Arizona")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label='Zip Code']").send_keys("85206")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label='email address']").send_keys(email_address)
    chrome_driver.find_element(By.XPATH, "//input[@aria-label='contact number']").send_keys("9762830899")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()  # enter survey
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()  # gender
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()  # cancer
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_trnsgndr = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'trnsgndr']"))
    sel_trnsgndr.select_by_visible_text("No")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()  # trans
    chrome_driver.find_element(By.XPATH,
                               "//input[@placeholder='Please enter a value in feet no less than 3 feet and no greater than 8 feet.']").send_keys(
        5.2)
    chrome_driver.find_element(By.XPATH,
                               "//input[@placeholder='Please enter a value in inches no less than 0 inches and no greater than 11 inches.']").send_keys(
        11.5)
    chrome_driver.find_element(By.XPATH, "//div[@ng-style = 'getFlexDirectionStyle()']/div[8]//input[@type='number']").send_keys(150.5)
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()  # height
    sel_weightdesc = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'weightdesc']"))
    sel_weightdesc.select_by_visible_text("My weight is just right")
    sel_weightgoals = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'weightgoals']"))
    sel_weightgoals.select_by_visible_text("Gain weight")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()  # weight
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # Race
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # Ethnicity
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_income = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'incomeranges']"))
    sel_income.select_by_visible_text("$10,000 to $14,999")
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # born in usa
    chrome_driver.find_element(By.XPATH,
                               "//*[@id='formPageContainer']/div[2]/container-flex-wrapper/div/div/div/div/preview-form-section/div/container-flex-wrapper/div/div/div/div/preview-form-component/div/container-flex-wrapper/div/div/div/div[4]//div/div[1]/div/div/preview-sub-field-multi-select-option-value/div/label/div[2]").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class='display-flex']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_maritalstatus = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'maritalstatus']"))
    sel_maritalstatus.select_by_visible_text("Married")
    sel_occupationstatus = Select(chrome_driver.find_element(By.XPATH, "//select[@title = 'occupationstatus']"))
    sel_occupationstatus.select_by_visible_text("Employed (Full-time)")
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys(10)
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()

@pytest.mark.skip
def test_submit_mtl_order():
    chrome_driver = webdriver.Chrome()
    email_address1 = 'pdaundkar9+2405151842@gmail.com'
    password1 = 'Test@123'
    chrome_driver.get(login_url)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address1)
    chrome_driver.find_element(By.ID, "password").send_keys(password1)
    chrome_driver.find_element(By.ID, "action-button").click()
    time.sleep(5)
    chrome_driver.find_element(By.XPATH, "//div/container-card[2]//span[@class='ng-binding']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()


@pytest.mark.skip
def test_survey_response_yes_positive_all():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(login_url)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.XPATH, "//button[@aria-label = 'Start']").click()
    time.sleep(5)
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class= 'table-wrap']/div[1]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 150)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[3]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[4]//div[@ng-if = 'shouldShowLeftImage()']").click()
    for i in range(9):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()

    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()

@pytest.mark.skip
def test_survey_response_yes_positive_for_t1():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(login_url)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.XPATH, "//button[@aria-label = 'Start']").click()
    time.sleep(5)
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class= 'table-wrap']/div[1]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 150)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()

    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()

@pytest.mark.skip
def test_survey_response_negative():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://together4healthva-vrp-edge.qak8s.vibrenthealth.com/login")
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.XPATH, "//button[@aria-label = 'Start']").click()
    time.sleep(5)
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class= 'table-wrap']/div[1]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 150)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[5]//div[@ng-if = 'shouldShowLeftImage()']").click()
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()


@pytest.mark.skip
def test_survey_response_inconclusive_both_test_result():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://together4healthva-vrp-edge.qak8s.vibrenthealth.com/login")
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.XPATH, "//button[@aria-label = 'Start']").click()
    time.sleep(5)
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class= 'table-wrap']/div[1]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 1000)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[6]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@aria-label = 'text-label']/p/span").click()  # select another test
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 1000)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[6]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()

@pytest.mark.skip
def test_survey_response_inconclusive_first_negative_second():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://together4healthva-vrp-edge.qak8s.vibrenthealth.com/login")
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.XPATH, "//button[@aria-label = 'Start']").click()
    time.sleep(5)
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class= 'table-wrap']/div[1]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 1000)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[6]//div[@ng-if = 'shouldShowLeftImage()']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@aria-label = 'text-label']/p/span").click()  # select another test
    sel_barcode = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_barcode.select_by_visible_text("constant_" + str(random.randint(1, 1000)))
    for i in range(8):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowLeftImage()']").click()  # 15 mins
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[2]//div[@ng-if = 'shouldShowLeftImage()']").click()  # 20 mins
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH,
                               "//div[@class = 'table-wrap']/div[5]//div[@ng-if = 'shouldShowLeftImage()']").click()
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()


def test_allow_ehr_access_community_health_network_epic_dstu2():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(login_url)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "emailOrPhone").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.XPATH, "//nav[@class='navigation-container']/ul/li[5]").click()
    chrome_driver.find_element(By.XPATH, "//div[@ui-view = 'content']/div/container-card[2]//span[@class='ng-binding']").click()
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//div[@aria-label = 'Access Community Health Network']").click()
    for i in range(3):
        chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|continue']").click()
    time.sleep(20)
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    chrome_driver.find_element(By.ID, "Login").send_keys("fhircamila")
    chrome_driver.find_element(By.ID, "Password").send_keys("epicepic1")
    chrome_driver.find_element(By.ID, "submit").click()
    WebDriverWait(chrome_driver, 50).until(
        EC.element_to_be_clickable((By.ID, "nextButton")))
    chrome_driver.find_element(By.ID, "nextButton").click()
    chrome_driver.find_element(By.ID, "allowDataSharing").click()
    WebDriverWait(chrome_driver, 50).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Continue']")))
    chrome_driver.find_element(By.XPATH, "//button[@title='Continue']").click()
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    chrome_driver.switch_to.default_content()
    chrome_driver.find_element(By.XPATH, "//button[@data-target='@form|button|submit']").click()
    print("test")

