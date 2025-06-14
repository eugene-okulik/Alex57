from selenium.webdriver.common.by import By


def test_submit_text(driver):
    input_data = 'sfsdfsdfsdfsdfsd'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    submit_text = driver.find_element(By.ID, 'result-text').text
    assert input_data == submit_text
    print(submit_text)
