from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):

    quantity_items = None
    number_item_products_one_page = None
    text_gear = None

    page_url = '/sale.html'

    def check_text_page_sale(self, text1, text2):
        text_sale = self.find(loc.base_loc)
        expect(text_sale).to_be_visible()
        expect(text_sale).to_have_text(text1)
        text_categories_menu = self.find(
            loc.text_categories_menu_loc)
        expect(text_categories_menu).to_contain_text(text2)

    def page_women_sale(self, text):
        link_women_deals = self.find(loc.link_women_deals_loc)
        link_women_deals.hover()
        link_women_deals.click()
        text_page_women_sale = self.find(loc.text_page_women_sale_loc)
        expect(text_page_women_sale).to_have_text(text)

    def check_quantity_items_in_pages(self):
        self.quantity_items = self.find(loc.quantity_items_loc)
        item_products_one_page = self.find_all(loc.item_products_one_page_loc)
        self.number_item_products_one_page = str(len(item_products_one_page))
        button_next = self.find(loc.button_next_loc)
        button_next.hover()
        button_next.click()

    def comparison_item_pages(self):
        self.page.wait_for_timeout(1000)
        products = self.find(loc.product_item_link_loc).first
        expect(products).to_be_visible()
        expect(self.quantity_items).to_have_text(
            self.number_item_products_one_page)

    def click_page_gear(self):
        link_gear_steals = self.find(loc.link_gear_steals_loc)
        link_gear_steals.hover()
        link_gear_steals.click()
        self.text_gear = self.find(loc.base_loc)

    def check_in_text_page_gear(self, text1, text2):
        expect(self.text_gear).to_have_text(text1)
        sidebar_main = self.find(loc.sidebar_sidebar_main_loc)
        expect(sidebar_main).to_be_visible()
        text_menu = self.find(loc.text_menu_loc)
        # Разбиваем text2 на строки и проверяем каждую значимую строку
        lines = text2.split('\n')
        for line in lines:
            if line.strip():  # проверяем только непустые строки
                expect(text_menu).to_contain_text(line.strip())

    def click_page_bags(self):
        menu_gear = self.find(loc.menu_gear_loc)
        menu_gear.hover()
        link_bags = self.find(loc.link_bags_loc)
        link_bags.hover()
        link_bags.click()
        text_page_bags = self.find(loc.base_loc).inner_text()
        expect(link_bags).to_have_text(text_page_bags)

    def click_page_fitness_equipment(self):
        menu_gear = self.find(loc.menu_gear_loc)
        menu_gear.hover()
        link_fitness_equipment = self.find(loc.link_fitness_equipment_loc)
        link_fitness_equipment.hover()
        link_fitness_equipment.click()
        text_page_fitness_equipment = self.find(loc.base_loc).inner_text()
        expect(link_fitness_equipment).to_have_text(
            text_page_fitness_equipment)

    def click_page_watches(self):
        menu_gear = self.find(loc.menu_gear_loc)
        menu_gear.hover()
        link_watches = self.find(loc.link_watches_loc)
        link_watches.hover()
        link_watches.click()
        text_page_watches = self.find(loc.base_loc).inner_text()
        expect(link_watches).to_have_text(text_page_watches)
