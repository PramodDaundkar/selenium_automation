import datetime

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

email_address = "vhtests+" + datetime.datetime.now().strftime("%y%m%d%H%M") + "@gmail.com"
password = "Test@123"
logger.info(email_address)
logger.info(password)

def test_complete_signup():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://pmi-pmi-edge.qak8s.vibrenthealth.com/")
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.ID, "email").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys(password)
    chrome_driver.find_element(By.ID, "action-button").click()
    chrome_driver.find_element(By.NAME, "verification_code")
    time.sleep(5)

    element = WebDriverWait(chrome_driver, 50).until(EC.element_to_be_clickable((By.ID, "action-button"))
                                                     )
    chrome_driver.find_element(By.ID, "action-button").click()
    # driver.switch_to.alert.accept()
    element1 = WebDriverWait(chrome_driver, 50).until(
        EC.element_to_be_clickable((By.ID, "zipCode"))
    )
    # Pittsburg 532 S. Aiken Ave,Suite 209,Pittsburgh,PA,15232
    chrome_driver.find_element(By.ID, "zipCode").send_keys("15232")

    chrome_driver.find_element(By.ID, 'addZipCodeContinueButton').click()
    chrome_driver.find_element(By.ID, "beginYourJournyContinueButton").click()
    print(chrome_driver.find_element(By.XPATH, "//span[@class = 'container-header']/span").text)
    assert chrome_driver.title == 'Dashboard'


@pytest.mark.skip
def test_login_complete_primary_consent():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://pmi-pmi-edge.qak8s.vibrenthealth.com/login")
    chrome_driver.implicitly_wait(30)
    chrome_driver.find_element(By.XPATH, "//input[@id='emailOrPhone']").send_keys(email_address)
    chrome_driver.find_element(By.ID, "password").send_keys("Test@123")
    chrome_driver.find_element(By.XPATH, "//button[@type='submit']").click()
    chrome_driver.find_element(By.XPATH, "//button[@title = 'Start']").click()
    element_scroll_pageend = chrome_driver.find_element(By.ID, 'pageEnd')
    act = ActionChains(chrome_driver)
    act.move_to_element(element_scroll_pageend).click_and_hold().perform()

    for i in range(3):
        chrome_driver.find_element(By.XPATH,
                                   "//button[@data-target = '@form|button|continue']").click()  # video, 2nd, 3rd, 4th, 5th

    sel_state = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'select']"))
    sel_state.select_by_visible_text("Pennsylvania")

    sel_healthcare = Select(chrome_driver.find_element(By.XPATH,
                                                       "//*[@id='formPageContainer']/div[2]/container-flex-wrapper/div/div/div/div[2]/preview-form-section/div/container-flex-wrapper/div/div/div/div/preview-form-component/div/container-flex-wrapper/div/div/div/div[1]//select"))
    sel_healthcare.select_by_visible_text("Pennsylvania")

    chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()  # 6th
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()

    for i in range(3):
        print(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
        logging.getLogger(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
        logging.info(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
        chrome_driver.find_element(By.XPATH,
                                   "//button[@data-target = '@form|button|continue']").click()  # 8th, 9th, 10th

    for i in range(9):
        print(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
        element_scroll_pageend = chrome_driver.find_element(By.ID, 'pageEnd')
        act = ActionChains(chrome_driver)
        act.move_to_element(element_scroll_pageend).click_and_hold().perform()
        chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()

    chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()

    for i in range(2):
        print(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
        element_scroll_pageend = chrome_driver.find_element(By.ID, 'pageEnd')
        act = ActionChains(chrome_driver)
        act.move_to_element(element_scroll_pageend).click_and_hold().perform()
        # driver.find_element(By.XPATH, "//div[@aria-label = 'Show transcript']").click()
        chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()

    print(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
    element_scroll_pageend = chrome_driver.find_element(By.ID, 'pageEnd')
    act = ActionChains(chrome_driver)
    act.move_to_element(element_scroll_pageend).click_and_hold().perform()
    # driver.find_element(By.XPATH, "//div[@aria-label = 'Show transcript']").click()
    chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()

    for i in range(6):
        print(chrome_driver.find_element(By.XPATH, "//h2/strong/span").text)
        chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()

    element_scroll_pageend = chrome_driver.find_element(By.ID, 'pageEnd')
    # driver.execute_script("arguments[0].click();", element_scroll_pageend)

    act = ActionChains(chrome_driver)
    act.move_to_element(element_scroll_pageend).click_and_hold().perform()
    chrome_driver.find_element(By.XPATH, "//div[@ng-if = 'shouldShowText()']").click()
    chrome_driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("Pramod")
    chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|continue']").click()
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'first name']").send_keys("Pramod")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'middle name']").send_keys("B")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'last name']").send_keys("Daundkar")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'address 1']").send_keys("532 S. Aiken Ave")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'address 2']").send_keys("Pittsburgh")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'city']").send_keys("Pennsylvania ")
    sel_state = Select(chrome_driver.find_element(By.XPATH, "//select[@aria-label = 'state']"))
    sel_state.select_by_visible_text("Pennsylvania")
    chrome_driver.find_element(By.XPATH, "//input[@aria-label = 'phone number']").send_keys("9762830899")
    chrome_driver.find_element(By.XPATH, "//input[@ui-mask-placeholder = 'mm/dd/yyyy']").send_keys("05/05/1972")
    for i in range(2):
        chrome_driver.find_element(By.XPATH, "//button[@data-target = '@form|button|submit']").click()
    print("Primary Consent Completed")
    time.sleep(10)
