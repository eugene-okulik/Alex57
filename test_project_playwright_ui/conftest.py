import pytest
from pages.customer_account import CustomerAccount
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def page(browser):
    page = browser.new_page(
        viewport={'width': 1920, 'height': 1080}
    )
    return page


@pytest.fixture()
def account_page(page):
    return CustomerAccount(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendlyPage(page)
