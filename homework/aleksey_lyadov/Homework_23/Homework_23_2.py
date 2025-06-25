from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_fill_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    fill_first_name = driver.find_element(By.ID, 'firstName')
    fill_first_name.send_keys('Alexey')
    fill_last_name = driver.find_element(By.ID, 'lastName')
    fill_last_name.send_keys('Lyadov')
    fill_email = driver.find_element(By.ID, 'userEmail')
    fill_email.send_keys('qa@mail.ru')
    choose_gender = driver.find_element(
        By.CSS_SELECTOR, '#gender-radio-1')
    driver.execute_script("arguments[0].click();", choose_gender)
    fill_mobile = driver.find_element(By.ID, 'userNumber')
    fill_mobile.send_keys('9730008989')
    choose_date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    choose_date_of_birth.click()
    choose_month = driver.find_element(
        By.CSS_SELECTOR,
        '.react-datepicker__month-select > option:nth-child(5)')
    choose_month.click()
    choose_year = driver.find_element(
        By.CSS_SELECTOR,
        '.react-datepicker__year-select > option:nth-child(90)')
    choose_year.click()
    choose_day = driver.find_element(
        By.CSS_SELECTOR,
        '[class="react-datepicker__day react-datepicker__day--017"]')
    choose_day.click()
    fill_subjects = driver.find_element(
        By.CSS_SELECTOR, '#subjectsInput')
    driver.execute_script("arguments[0].click();", fill_subjects)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, '#subjectsInput')))
    actions = ActionChains(driver)
    actions.click_and_hold(fill_subjects).perform()
    fill_subjects.send_keys('Physics')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#react-select-2-option-0')))
    driver.find_element(
        By.CSS_SELECTOR,
        '#react-select-2-option-0').click()
    choose_hobbies = driver.find_element(
        By.CSS_SELECTOR, '#hobbies-checkbox-3')
    driver.execute_script("arguments[0].click();", choose_hobbies)
    choose_current_address = driver.find_element(By.ID, 'currentAddress')
    choose_current_address.send_keys('Orel')
    driver.execute_script("window.scrollTo(200, 700)")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, 'div[id="state"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="react-select-3-option-0"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, 'div[id="city"]'))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-select-4-option-0"]'))).click()
    driver.find_element(By.ID, 'submit').click()
    form_text = driver.find_element(
        By.CLASS_NAME, 'modal-body').get_attribute('innerText')
    print(form_text)
