from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import customer_account_locators as loc


class CustomerAccount(BasePage):

    page_url = '/customer/account/create/'

    def fill_login_form(
            self, first_name, last_name,
            password, confirm_password, email=None):
        field_first_name = self.find(loc.field_first_name_loc)
        field_last_name = self.find(loc.field_last_name_loc)
        email_address = self.find(loc.email_address_loc)
        field_password = self.find(loc.field_password_loc)
        field_confirm_password = self.find(loc.field_confirm_password_loc)
        button = self.find(loc.button_loc)
        field_first_name.press_sequentially(first_name, delay=300)
        field_last_name.press_sequentially(last_name, delay=300)
        if email is not None:
            email_address.press_sequentially(email, delay=300)
        field_password.press_sequentially(password, delay=300)
        field_confirm_password.press_sequentially(confirm_password, delay=300)
        button.click()

    def check_text_in_page_bad_add_account_registration(self, text1, text2):
        password_error = self.find(loc.password_error_loc)
        expect(password_error).to_be_visible()
        email_address_error = self.find(loc.email_address_error_loc)
        expect(password_error).to_have_text(text1)
        expect(email_address_error).to_have_text(text2)

    def check_text_in_page_add_account_registration(self, text):
        success_message = self.find(loc.success_message_loc)
        expect(success_message).to_be_visible()
        expect(success_message).to_have_text(text)

    def check_text_account(self, text):
        text_website = self.find(loc.text_website_loc)
        expect(text_website).to_contain_text(text)
