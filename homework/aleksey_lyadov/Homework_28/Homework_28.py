from playwright.sync_api import Page, Route, expect
import re
import json


def test_apple_shop(page: Page):
    def changing_title(route: Route):
        print("Intercepted URL:", route.request.url)
        response = route.fetch()
        body = response.json()
        # Модифицируем productName во всех нужных местах
        if 'body' in body and 'digitalMat' in body['body']:
            digital_mat = body['body']['digitalMat']
            # Изменяем productName в корне digitalMat
            if isinstance(digital_mat, list) and len(digital_mat) > 0:
                digital_mat[0]['productName'] = 'яблокофон 16 про'
                # Изменяем productName внутри familyTypes
                if 'familyTypes' in digital_mat[0]:
                    for family_type in digital_mat[0]['familyTypes']:
                        family_type['productName'] = 'яблокофон 16 про'
                        # Изменяем linkText в productLink
                        if ('productLink' in family_type
                                and 'link' in family_type['productLink']):
                            family_type[
                                'productLink'][
                                'link'][
                                'text'] = 'яблокофон 16 про'
                            if ('omnitureData' in
                                    family_type['productLink']['link']):
                                family_type[
                                    'productLink'][
                                    'link'][
                                    'omnitureData'][
                                    'linkText'] = 'яблокофон 16 про'
                        # Изменяем tabTitle
                        if 'tabTitle' in family_type:
                            family_type['tabTitle'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(
        re.compile(
            r'api/digital-mat\?path=library/'
            r'step0_iphone/digitalmat'), changing_title)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator(
        '[class="rf-hcard-content tile as-util-relatedlink"]'
    ).locator('nth=0').click()
    text_in_popap = page.locator(
        '[id="rf-digitalmat-overlay-label-0"]').locator('nth=0')
    expect(text_in_popap).to_have_text('яблокофон 16 про')
