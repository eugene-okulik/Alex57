from playwright.sync_api import Page, Route
import re
from time import sleep


def test_apple_shop(page: Page):

    def changing_title(route: Route):
        url = route.request.url
        print(url)
        url = url.replace(
            '%7CiPhone%2016%C2%A0Pro', '%7Cяблокофон%2016%C2%A0про')
        route.continue_(url=url)

    page.route(
        re.compile(
            'securemetrics.apple.com/b/ss/applestoreww/'), changing_title)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator(
        '[class="rf-hcard-content tile as-util-relatedlink"]'
    ).locator('nth=0').click()
    text_in_popap = page.locator(
        '[id="rf-digitalmat-overlay-label-0"]').locator('nth=0')
    text_in_popap.click()
    # expect(text_in_popap).to_have_text('iPhone 16 Pro')
    sleep(5)
