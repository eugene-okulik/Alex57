from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


def test_product_store(driver):
    driver.get('https://www.demoblaze.com/index.html')
    nokia_lumia = driver.find_element(
        By.CSS_SELECTOR, '[href="prod.html?idp_=2"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(nokia_lumia)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    name = driver.find_element(By.CLASS_NAME, 'name').text
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="btn btn-success btn-lg"]'))).click()
    alert = Alert(driver)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()
    name_product = driver.find_element(
        By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(2)').text
    assert name == name_product


def test_luma(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    one_product = driver.find_element(By.CSS_SELECTOR, '[alt="Push It Messenger Bag"]')
    button_add_compare = driver.find_element(By.CSS_SELECTOR, '[class="action tocompare"]')
    actions = ActionChains(driver)
    actions.move_to_element(one_product).perform()
    actions.move_to_element(button_add_compare)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="action tocompare"]')))
    actions.double_click(button_add_compare).perform()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#compare-items > li > a > span')))
    text_verification = driver.find_element(
        By.CSS_SELECTOR, '#compare-items > li > a > span').get_attribute('innerText')
    assert text_verification == 'Remove This Item'
