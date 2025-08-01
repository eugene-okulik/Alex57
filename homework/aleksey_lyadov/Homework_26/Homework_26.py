from playwright.sync_api import Page


def test_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    user_name = page.get_by_role('textbox', name='username')
    user_name.fill('test57')
    user_pass = page.get_by_role('textbox', name='password')
    user_pass.press_sequentially('64564dgdfsAA', delay=300)
    button_authorize = page.get_by_role('button', name='Login')
    button_authorize.click()


def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    fill_first_name = page.get_by_placeholder('First Name')
    fill_first_name.fill('Test')
    fill_last_name = page.locator('#lastName')
    fill_last_name.fill('Testova')
    fill_email = page.locator('#userEmail')
    fill_email.fill('qa@mail.ru')
    choose_gender = page.locator('label[for="gender-radio-2"]')
    choose_gender.check()
    fill_mobile = page.locator('#userNumber')
    fill_mobile.fill('9730008989')
    page.locator('#dateOfBirthInput').click()
    page.locator(
        '.react-datepicker__month-select').select_option('4')
    page.locator(
        '.react-datepicker__year-select').select_option('2000')
    page.locator(
        '.react-datepicker__day--005:not('
        '.react-datepicker__day--outside-month)').click()
    fill_subjects = page.locator('#subjectsInput')
    fill_subjects.click()
    fill_subjects.fill('Physics')
    page.locator('#react-select-2-option-0').click()
    choose_hobbies = page.locator(
        'label[for="hobbies-checkbox-3"]')
    choose_hobbies.check()
    choose_current_address = page.locator('#currentAddress')
    choose_current_address.fill('Orel')
    page.locator('[id="state"]').click()
    page.locator('//*[@id="react-select-3-option-0"]').click()
    page.locator('div[id="city"]').click()
    page.locator('//*[@id="react-select-4-option-0"]').click()
    page.locator('#submit').click()
