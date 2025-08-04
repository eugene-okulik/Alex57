from playwright.sync_api import Page, expect, BrowserContext


# Задание №1
def test_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    text = page.locator('#result-text')
    expect(text).to_have_text('Ok')


# Задание №2
def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link_new_page = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        link_new_page.click()
    new_page = new_page_event.value
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(link_new_page).to_be_enabled()


# Задание №3
def test_button_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_class = page.locator('[class="mt-4 text-danger btn btn-primary"]')
    # В styles color: #dc3545 его rgb(220, 53, 69)
    expect(color_class).to_have_css('color', 'rgb(220, 53, 69)')
    color_class.click()
