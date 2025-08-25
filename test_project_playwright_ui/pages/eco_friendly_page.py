from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import eco_friendly_page_locators as loc


class EcoFriendlyPage(BasePage):

    text_one_page = None
    text_two_page = None
    size_text = None
    color_text = None
    text_one = None

    page_url = '/collections/eco-friendly.html'

    def add_cart(self):
        choice_bella_tank = self.find(loc.choice_bella_tank_loc)
        self.text_one_page = self.find(
            loc.text_one_page_loc)
        choice_bella_tank.hover()
        choice_bella_tank.click()
        size = self.find(loc.size_loc)
        expect(size).to_be_visible()
        color = self.find(loc.color_loc)
        size.click()
        expect(color).to_be_visible()
        color.click()
        button_add_to_cart = self.find(
            loc.button_add_to_cart_loc)
        expect(button_add_to_cart)
        button_add_to_cart.hover()
        button_add_to_cart.click()
        self.text_two_page = self.find(
            loc.text_two_page_loc).inner_text()
        self.size_text = self.find(
            loc.size_text_loc)
        self.color_text = self.find(
            loc.color_text_loc)

    def check_text_add_cart(self, text1, text2, text3, text4):
        text_add_cart = self.find(loc.data_bind_loc)
        counter_number = self.find(loc.counter_number_loc)
        expect(self.text_one_page).to_have_text(self.text_two_page)
        expect(self.size_text).to_have_text(text1)
        expect(self.color_text).to_have_text(text2)
        expect(text_add_cart).to_have_text(text3)
        expect(counter_number).to_have_text(text4)

    def add_compare(self):
        choice_bella_tank = self.find(loc.choice_bella_tank_loc)
        choice_bella_tank.hover()
        self.page.wait_for_timeout(1000)
        button_add_to_compare = self.find(loc.button_add_to_compare_loc)
        button_add_to_compare.hover()
        button_add_to_compare.click()
        self.text_one = self.find(loc.text_one_page_loc)

    def check_text_add_compare(self, text):
        text_two = self.find(
            loc.text_two_loc).inner_text()
        text_add_product = self.find(loc.data_bind_loc)
        expect(text_add_product).to_be_visible()
        expect(self.text_one).to_contain_text(text_two)
        expect(text_add_product).to_have_text(text)

    def add_wish_list(self, text):
        email = 'tesstqa@mail.ru'
        password = '12345aa!'
        choice_bella_tank = self.find(loc.choice_bella_tank_loc)
        expect(choice_bella_tank).to_be_visible()
        choice_bella_tank.hover()
        self.page.wait_for_timeout(1000)
        self.text_one_page = self.find(loc.text_one_page_loc)
        button_add_wish_list = self.find(loc.button_add_wish_list_loc)
        expect(button_add_wish_list).to_have_attribute('title', 'Add to Wish List')
        button_add_wish_list.click(force=True)
        text_page_login = self.find(
            loc.text_page_login_loc)
        expect(text_page_login).to_be_visible()
        expect(text_page_login).to_have_text(text)
        add_email = self.find(loc.add_email_loc)
        add_password = self.find(loc.add_password_loc)
        add_email.fill(email)
        add_password.fill(password)
        button_sign_in = self.find(loc.button_sign_in_loc)
        button_sign_in.click()

    def check_text_wish_list(self, text1, text2):
        text_add_wish_list = self.find(loc.text_add_wish_list_loc)
        text_pege_my_wish_list = self.find(loc.text_pege_my_wish_list_loc)
        text_two_page = self.find(loc.text_one_page_loc).inner_text()
        expect(text_add_wish_list).to_have_text(text1)
        expect(text_pege_my_wish_list).to_contain_text(text2)
        expect(self.text_one_page).to_contain_text(text_two_page)
