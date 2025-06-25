from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_language = driver.find_element(
        By.CSS_SELECTOR, '[name="choose_language"]')
    choose_language.click()
    option_language = driver.find_element(
        By.CSS_SELECTOR, '#id_choose_language > option:nth-child(3)').text
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '#id_choose_language > option:nth-child(3)'))).click()
    button_submit = driver.find_element(By.ID, 'submit-id-submit')
    button_submit.click()
    result_text = driver.find_element(By.ID, 'result-text').text
    assert option_language == result_text


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button_start = driver.find_element(By.CSS_SELECTOR, '#start > button')
    button_start.click()
    verifiable_text = driver.find_element(
        By.CSS_SELECTOR, '#finish > h4').text
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '#finish > h4')))
    assert verifiable_text == 'Hello World!'
