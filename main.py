import requests
import telebot

cookies = {
    '_ym_uid': '1618150302264108086',
    'MVID_CITY_ID': 'CityCZ_1638',
    'MVID_REGION_ID': '6',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_KLADR_ID': '7800000000000',
    'MVID_REGION_SHOP': 'S904',
    'tmr_lvid': '8e7a033af8ea41493c0c2d2473923b85',
    'tmr_lvidTS': '1618150301406',
    'afUserId': 'd5160f6e-4faf-47a3-aa9c-bbbe7e50eda4-p',
    'snActionRedirectUrl': '/login?snActionType=login&snProviderId=vkontakte&type=individual',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'MAIN_PAGE_VARIATION': '2',
    'MVID_AB_PROMO_DAILY': '1',
    'MVID_CATALOG_STATE': '1',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_FILTER_CODES': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GIFT_KIT': 'true',
    'MVID_GUEST_ID': '20613190696',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
    'MVID_WEBP_ENABLED': 'true',
    'admitad_deduplication_cookie': 'google__organic',
    '__SourceTracker': 'google__organic',
    '_ym_d': '1651406215',
    'mindboxDeviceUUID': '6e6f00e6-d6c9-47da-afa5-526b7f4df5e7',
    'directCrm-session': '%7B%22deviceGuid%22%3A%226e6f00e6-d6c9-47da-afa5-526b7f4df5e7%22%7D',
    '__ttl__widget__ui': '1651406279194-500667179e85',
    '_ga': 'GA1.1.903596161.1634501129',
    'tmr_reqNum': '1868',
    '_ga_CFMZTSS5FM': 'GS1.1.1651406212.32.1.1651406289.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1651406212.32.1.1651406289.49',
    '__lhash_': 'aa781fd4ad904c53b410fed4a22bd9d7',
    'COMPARISON_INDICATOR': 'false',
    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_HANDOVER_SUMMARY': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '1',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_SERVICES': '111',
    'MVID_SMART_BANNER_BOTTOM': 'true',
    'PICKUP_SEAMLESS_AB_TEST': '2',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'flacktory': 'no',
    'searchType2': '3',
    'wurfl_device_id': 'generic_web_browser',
    'JSESSIONID': 'wRHLjXpc187RC838TSw4fnRQPrHkJBq9QYDvHDvLr5C1FSLJdj8b!431163428',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'BIGipServeratg-ps-prod_tcp80': '1141169162.20480.0000',
    'bIPs': '-826759811',
    'MVID_GTM_BROWSER_THEME': '1',
    'deviceType': 'desktop',
    'BIGipServeratg-ps-prod_tcp80_clone': '1141169162.20480.0000',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VwXX05IW8hUkRdVCM4IRR/F0YeC0EhX2IVPUF2fy8oUHpIVyNlFWs1U3x+JGUqJ3Vxe3UtGj9oHmBNXCNFXT56Kx8Te3IoWA0PYUVFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdzdS1Cax1kT1snSlE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYVy9wJBdIUn47FmtuR2dHV0wXX0I7OFhBEXVbPUZtdi5EZiJhOVURCxIXRF5cVWl1ZxlMQFcvDS44Xi1vHmVLXyRMXlZ6JxsSfGcVHkBPG1AINDZicFcnKxEmVD9HGUplTnsJXWMTOEQhCXY9PxsQOg==GhP/ww==',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VwXX05IW8hUkRdVCM4IRR/F0YeC0EhX2IVPUF2fy8oUHpIVyNlFWs1U3x+JGUqJ3Vxe3UtGj9oHmBNXCNFXT56Kx8Te3IoWA0PYUVFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdzdS1Cax1kT1snSlE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYVy9wJBdIUn47FmtuR2dHV0wXX0I7OFhBEXVbPUZtdi5EZiJhOVURCxIXRF5cVWl1ZxlMQFcvDS44Xi1vHmVLXyRMXlZ6JxsSfGcVHkBPG1AINDZicFcnKxEmVD9HGUplTnsJXWMTOEQhCXY9PxsQOg==GhP/ww==',
    'cfidsgib-w-mvideo': 'XQdxfT5VD1tP2hp+Vk21y337IHLMnAcmpCkiJBOtuxE804FYiL7xyAh/x98cFBYQtAwpr6VvSJBu442oKmdi/TY1DzpzZFAFnxeC1ZRYsBEVsGwnMqMlhauHhgG4TLPsr7s/GzsTm6mm/FEZw0fhP8v9JbUn+8k2wLCGu/E=',
    'cfidsgib-w-mvideo': 'XQdxfT5VD1tP2hp+Vk21y337IHLMnAcmpCkiJBOtuxE804FYiL7xyAh/x98cFBYQtAwpr6VvSJBu442oKmdi/TY1DzpzZFAFnxeC1ZRYsBEVsGwnMqMlhauHhgG4TLPsr7s/GzsTm6mm/FEZw0fhP8v9JbUn+8k2wLCGu/E=',
    'gsscgib-w-mvideo': 'hD++E9lU6Kz8AXPmVmNAVbYN5WcWog0ddjZheqdK8cUi2J2qmyxudVJkZDCvkHsLoG50RAhAJjjNMO3BAMU8pMg3ZBtdmcKSW0ZW4xI+ACP6MbUFetUwe4F/qFfrI7RKWfT2m5Tub6WvTldrijRvGZtopHLv0IL3xkhfGsIlrk//CQZZzruMgZ4JC/cVtOYDJu5qsvGOcR3XpONxrBjO8b82/8QwCzfuxx71ZlUBYqyMOMth8yAsE96YbcBE5w==',
    'gsscgib-w-mvideo': 'hD++E9lU6Kz8AXPmVmNAVbYN5WcWog0ddjZheqdK8cUi2J2qmyxudVJkZDCvkHsLoG50RAhAJjjNMO3BAMU8pMg3ZBtdmcKSW0ZW4xI+ACP6MbUFetUwe4F/qFfrI7RKWfT2m5Tub6WvTldrijRvGZtopHLv0IL3xkhfGsIlrk//CQZZzruMgZ4JC/cVtOYDJu5qsvGOcR3XpONxrBjO8b82/8QwCzfuxx71ZlUBYqyMOMth8yAsE96YbcBE5w==',
    'fgsscgib-w-mvideo': 'FHScbdc2b059dbfe4f4516209c18ebe5fbdfc257',
    'fgsscgib-w-mvideo': 'FHScbdc2b059dbfe4f4516209c18ebe5fbdfc257',
    'cfidsgib-w-mvideo': '/X/jCBFbaTfje6rHu/yekqoOCYKtIJSzC/4P3tzgHg7Mk3sntWSjZ+XwtJT4mTqtlFTHeR84bDHH5sQ0clLwdM7szqeNhBmotNqZ9+HU1/XGOAiUK/UpDDAF/lPfzIMhiH0Xwy/En0kW3RMaY5DM2qXoBSxTpPLidg/fF1k=',
    'CACHE_INDICATOR': 'false',
    '__hash_': '43770020eebb4684bb5a8ec6a2593b72',
    'MVID_ENVCLOUD': 'prod2',
}

headers = {
    'authority': 'www.mvideo.ru',
    'accept': 'application/json',
    'accept-language': 'ru,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ym_uid=1618150302264108086; MVID_CITY_ID=CityCZ_1638; MVID_REGION_ID=6; MVID_TIMEZONE_OFFSET=3; MVID_KLADR_ID=7800000000000; MVID_REGION_SHOP=S904; tmr_lvid=8e7a033af8ea41493c0c2d2473923b85; tmr_lvidTS=1618150301406; afUserId=d5160f6e-4faf-47a3-aa9c-bbbe7e50eda4-p; snActionRedirectUrl=/login?snActionType=login&snProviderId=vkontakte&type=individual; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; MAIN_PAGE_VARIATION=2; MVID_AB_PROMO_DAILY=1; MVID_CATALOG_STATE=1; NEED_REQUIRE_APPLY_DISCOUNT=true; HINTS_FIO_COOKIE_NAME=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_FILTER_CODES=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20613190696; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; admitad_deduplication_cookie=google__organic; __SourceTracker=google__organic; _ym_d=1651406215; mindboxDeviceUUID=6e6f00e6-d6c9-47da-afa5-526b7f4df5e7; directCrm-session=%7B%22deviceGuid%22%3A%226e6f00e6-d6c9-47da-afa5-526b7f4df5e7%22%7D; __ttl__widget__ui=1651406279194-500667179e85; _ga=GA1.1.903596161.1634501129; tmr_reqNum=1868; _ga_CFMZTSS5FM=GS1.1.1651406212.32.1.1651406289.0; _ga_BNX5WPP3YK=GS1.1.1651406212.32.1.1651406289.49; __lhash_=aa781fd4ad904c53b410fed4a22bd9d7; COMPARISON_INDICATOR=false; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=true; MVID_CREDIT_AVAILABILITY=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=1; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_MBONUS_BLOCK=true; MVID_SERVICES=111; MVID_SMART_BANNER_BOTTOM=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=3; wurfl_device_id=generic_web_browser; JSESSIONID=wRHLjXpc187RC838TSw4fnRQPrHkJBq9QYDvHDvLr5C1FSLJdj8b!431163428; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=1141169162.20480.0000; bIPs=-826759811; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; BIGipServeratg-ps-prod_tcp80_clone=1141169162.20480.0000; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VwXX05IW8hUkRdVCM4IRR/F0YeC0EhX2IVPUF2fy8oUHpIVyNlFWs1U3x+JGUqJ3Vxe3UtGj9oHmBNXCNFXT56Kx8Te3IoWA0PYUVFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdzdS1Cax1kT1snSlE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYVy9wJBdIUn47FmtuR2dHV0wXX0I7OFhBEXVbPUZtdi5EZiJhOVURCxIXRF5cVWl1ZxlMQFcvDS44Xi1vHmVLXyRMXlZ6JxsSfGcVHkBPG1AINDZicFcnKxEmVD9HGUplTnsJXWMTOEQhCXY9PxsQOg==GhP/ww==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VwXX05IW8hUkRdVCM4IRR/F0YeC0EhX2IVPUF2fy8oUHpIVyNlFWs1U3x+JGUqJ3Vxe3UtGj9oHmBNXCNFXT56Kx8Te3IoWA0PYUVFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdzdS1Cax1kT1snSlE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYVy9wJBdIUn47FmtuR2dHV0wXX0I7OFhBEXVbPUZtdi5EZiJhOVURCxIXRF5cVWl1ZxlMQFcvDS44Xi1vHmVLXyRMXlZ6JxsSfGcVHkBPG1AINDZicFcnKxEmVD9HGUplTnsJXWMTOEQhCXY9PxsQOg==GhP/ww==; cfidsgib-w-mvideo=XQdxfT5VD1tP2hp+Vk21y337IHLMnAcmpCkiJBOtuxE804FYiL7xyAh/x98cFBYQtAwpr6VvSJBu442oKmdi/TY1DzpzZFAFnxeC1ZRYsBEVsGwnMqMlhauHhgG4TLPsr7s/GzsTm6mm/FEZw0fhP8v9JbUn+8k2wLCGu/E=; cfidsgib-w-mvideo=XQdxfT5VD1tP2hp+Vk21y337IHLMnAcmpCkiJBOtuxE804FYiL7xyAh/x98cFBYQtAwpr6VvSJBu442oKmdi/TY1DzpzZFAFnxeC1ZRYsBEVsGwnMqMlhauHhgG4TLPsr7s/GzsTm6mm/FEZw0fhP8v9JbUn+8k2wLCGu/E=; gsscgib-w-mvideo=hD++E9lU6Kz8AXPmVmNAVbYN5WcWog0ddjZheqdK8cUi2J2qmyxudVJkZDCvkHsLoG50RAhAJjjNMO3BAMU8pMg3ZBtdmcKSW0ZW4xI+ACP6MbUFetUwe4F/qFfrI7RKWfT2m5Tub6WvTldrijRvGZtopHLv0IL3xkhfGsIlrk//CQZZzruMgZ4JC/cVtOYDJu5qsvGOcR3XpONxrBjO8b82/8QwCzfuxx71ZlUBYqyMOMth8yAsE96YbcBE5w==; gsscgib-w-mvideo=hD++E9lU6Kz8AXPmVmNAVbYN5WcWog0ddjZheqdK8cUi2J2qmyxudVJkZDCvkHsLoG50RAhAJjjNMO3BAMU8pMg3ZBtdmcKSW0ZW4xI+ACP6MbUFetUwe4F/qFfrI7RKWfT2m5Tub6WvTldrijRvGZtopHLv0IL3xkhfGsIlrk//CQZZzruMgZ4JC/cVtOYDJu5qsvGOcR3XpONxrBjO8b82/8QwCzfuxx71ZlUBYqyMOMth8yAsE96YbcBE5w==; fgsscgib-w-mvideo=FHScbdc2b059dbfe4f4516209c18ebe5fbdfc257; fgsscgib-w-mvideo=FHScbdc2b059dbfe4f4516209c18ebe5fbdfc257; cfidsgib-w-mvideo=/X/jCBFbaTfje6rHu/yekqoOCYKtIJSzC/4P3tzgHg7Mk3sntWSjZ+XwtJT4mTqtlFTHeR84bDHH5sQ0clLwdM7szqeNhBmotNqZ9+HU1/XGOAiUK/UpDDAF/lPfzIMhiH0Xwy/En0kW3RMaY5DM2qXoBSxTpPLidg/fF1k=; CACHE_INDICATOR=false; __hash_=43770020eebb4684bb5a8ec6a2593b72; MVID_ENVCLOUD=prod2',
    'origin': 'https://www.mvideo.ru',
    'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914/brand=apple/tolko-v-nalichii=da/vstroennaya-pamyat=256gb/collection_top=iphone-13-pro---13-pro-max',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36',
    'x-set-application-id': 'd6e2b5f7-315d-4e07-89a1-ed6a54e32f7e',
}

json_data = {
    'productIds': [
        '30063191',
        '30063591',
        '30063588',
        '30063590',
        '30063589',
        '400007541',
        '400007535',
        '400007561',
        '400007550',
    ],
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,
}

response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

products = response.get('body').get('products')
result = {}
for p in products:
    if p['supplier'] is None:
        result.setdefault(p['productId'], [f"{p['name']}\n"])

cookies = {
    '__lhash_': '56c608935fb86f2308dc38b396a89b21',
    'COMPARISON_INDICATOR': 'false',
    'HINTS_FIO_COOKIE_NAME': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_1638',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GIFT_KIT': 'true',
    'MVID_GUEST_ID': '21390426371',
    'MVID_HANDOVER_SUMMARY': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '7800000000000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '6',
    'MVID_REGION_SHOP': 'S904',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PICKUP_SEAMLESS_AB_TEST': '2',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'searchType2': '3',
    '_ym_uid': '1658478316739982071',
    '_ym_d': '1662388356',
    '__ttl__widget__ui': '1662388356317-cfabcea699a6',
    'tmr_lvid': 'dad78e0a8eaebb0c46c7bb8a0f7f4942',
    'tmr_lvidTS': '1658478319235',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': 'd1037375-8e2a-40ce-ba74-63c910759fa1',
    'advcake_track_id': '3f021fb2-ed66-8717-53f3-7d94e7d45019',
    'advcake_session_id': 'f65bb683-d522-a3aa-1f86-bff0cefb39ca',
    'cookie_ip_add': '85.235.196.58',
    'afUserId': '8bcf331d-0747-46bc-abef-641beadb5762-p',
    'flocktory-uuid': '40b2008d-f936-4423-b3fb-ea562403999b-2',
    'AF_SYNC': '1662388359780',
    '__hash_': 'bee7e86626b8a0321bbe3738f1364145',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_SMART_BANNER_BOTTOM': 'true',
    'flacktory': 'no',
    '_sp_ses.d61c': '*',
    '_gid': 'GA1.2.556790890.1662553835',
    '_dc_gtm_UA-1873769-1': '1',
    '_ym_isad': '2',
    'wurfl_device_id': 'generic_web_browser',
    'JSESSIONID': 'SXZCjYTTDCvRKBvdjqJSdSX8LMlHNHVXn9b462BJ8pYLqjc7ZNcT!1834387723',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'BIGipServeratg-ps-prod_tcp80': '1157946378.20480.0000',
    'bIPs': '-1178626581',
    'MVID_GTM_BROWSER_THEME': '1',
    'deviceType': 'desktop',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VMYxcwIXB9Q1doGyNAK1czLWRpKj9+ZUkRGGVTCzUNbx8odVlTezczGT8cPxhBPmJnXygfGjxtIGNKYSZKV1BqJh8XeXAoUg8OYz9CdGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStAaiBnSmIlRlVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=8hS0xg==',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VMYxcwIXB9Q1doGyNAK1czLWRpKj9+ZUkRGGVTCzUNbx8odVlTezczGT8cPxhBPmJnXygfGjxtIGNKYSZKV1BqJh8XeXAoUg8OYz9CdGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStAaiBnSmIlRlVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=8hS0xg==',
    'SMSError': '',
    'authError': '',
    'cfidsgib-w-mvideo': 'w1UINpPhTtJuTblhPH3ZMTAbyibO1mxLbpNJL0XWEvLhmugCupypbTfTsfwNm0+eR2x/2TTxy2oma1OxNQkoS5fOP2nGuq5uiLEtoOlA/6VdrHvPnhGtOnO7jOWXhgPx7hAQ8NOjHoK6letjf4dDOePbJzHQfu7t22kx',
    'cfidsgib-w-mvideo': 'w1UINpPhTtJuTblhPH3ZMTAbyibO1mxLbpNJL0XWEvLhmugCupypbTfTsfwNm0+eR2x/2TTxy2oma1OxNQkoS5fOP2nGuq5uiLEtoOlA/6VdrHvPnhGtOnO7jOWXhgPx7hAQ8NOjHoK6letjf4dDOePbJzHQfu7t22kx',
    'gsscgib-w-mvideo': 'Prpw+lnkZslgeoPXJwohlyrzMvKEzYeHSP1Rr5q2dUmbzCvBbQPA+kYRo24OeSeudbY/fybK6iIYkqfUhUu9EFfV/SqIY27T1vOl8VMOTtPbCCJYVA2+NdS5kItfs5z/muW24C6ldDfbrR5SuJJDG46abwW+mdAlEdzhS6r6Un6wrTJeA99TLfeowJT5SEUR7Al5yqzKwE1hzN7stNZ35wsJ+TLHfdxKMFwjMiU0fudUWhmcNPNexoA9dT3nMw==',
    'gsscgib-w-mvideo': 'Prpw+lnkZslgeoPXJwohlyrzMvKEzYeHSP1Rr5q2dUmbzCvBbQPA+kYRo24OeSeudbY/fybK6iIYkqfUhUu9EFfV/SqIY27T1vOl8VMOTtPbCCJYVA2+NdS5kItfs5z/muW24C6ldDfbrR5SuJJDG46abwW+mdAlEdzhS6r6Un6wrTJeA99TLfeowJT5SEUR7Al5yqzKwE1hzN7stNZ35wsJ+TLHfdxKMFwjMiU0fudUWhmcNPNexoA9dT3nMw==',
    '_dc_gtm_UA-1873769-37': '1',
    'fgsscgib-w-mvideo': '1VNFa0d3a84c7cb327bb095aad8c981621a99731',
    'fgsscgib-w-mvideo': '1VNFa0d3a84c7cb327bb095aad8c981621a99731',
    'cfidsgib-w-mvideo': 'rkeSyPxtiySrgelzKzPM6CINhkMK8zlpbgt9HvLx04xgT4xXf1fom/0uGj5QuVrem67HB+7MLXbdBmfO06lBVjxmVK1GsUVC0Q/x0CRI2lF9H9z7vH+DC3usUUZJuPoe7w6YIcmxXU7l6IG/V4SUwPH8maxncTZz/US8',
    'CACHE_INDICATOR': 'false',
    '_sp_id.d61c': 'f5d929a1-3eb4-453c-91ba-79c13731c80f.1662388356.2.1662553844.1662388356.ba144132-79cd-4ee2-9ac4-73ab28923e9b.9e0a970d-6f69-4095-bae0-32eac316caa0.113b02fc-eb2a-42a4-aed8-93e51d0841a2.1662553835395.3',
    '_ga': 'GA1.2.1028379010.1662388356',
    'tmr_detect': '0%7C1662553852846',
    'tmr_reqNum': '65',
    '_ga_CFMZTSS5FM': 'GS1.1.1662553838.2.1.1662553874.0.0.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1662553838.2.1.1662553874.24.0.0',
    'MVID_ENVCLOUD': 'prod1',
}

headers = {
    'authority': 'www.mvideo.ru',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=8e66cbf3dbf942878d2efa1bcfae6d04,sentry-sample_rate=0%2C5',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__lhash_=56c608935fb86f2308dc38b396a89b21; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1638; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21390426371; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7800000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=6; MVID_REGION_SHOP=S904; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=3; _ym_uid=1658478316739982071; _ym_d=1662388356; __ttl__widget__ui=1662388356317-cfabcea699a6; tmr_lvid=dad78e0a8eaebb0c46c7bb8a0f7f4942; tmr_lvidTS=1658478319235; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=d1037375-8e2a-40ce-ba74-63c910759fa1; advcake_track_id=3f021fb2-ed66-8717-53f3-7d94e7d45019; advcake_session_id=f65bb683-d522-a3aa-1f86-bff0cefb39ca; cookie_ip_add=85.235.196.58; afUserId=8bcf331d-0747-46bc-abef-641beadb5762-p; flocktory-uuid=40b2008d-f936-4423-b3fb-ea562403999b-2; AF_SYNC=1662388359780; __hash_=bee7e86626b8a0321bbe3738f1364145; MVID_CREDIT_AVAILABILITY=true; MVID_SMART_BANNER_BOTTOM=true; flacktory=no; _sp_ses.d61c=*; _gid=GA1.2.556790890.1662553835; _dc_gtm_UA-1873769-1=1; _ym_isad=2; wurfl_device_id=generic_web_browser; JSESSIONID=SXZCjYTTDCvRKBvdjqJSdSX8LMlHNHVXn9b462BJ8pYLqjc7ZNcT!1834387723; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=1157946378.20480.0000; bIPs=-1178626581; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VMYxcwIXB9Q1doGyNAK1czLWRpKj9+ZUkRGGVTCzUNbx8odVlTezczGT8cPxhBPmJnXygfGjxtIGNKYSZKV1BqJh8XeXAoUg8OYz9CdGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStAaiBnSmIlRlVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=8hS0xg==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VMYxcwIXB9Q1doGyNAK1czLWRpKj9+ZUkRGGVTCzUNbx8odVlTezczGT8cPxhBPmJnXygfGjxtIGNKYSZKV1BqJh8XeXAoUg8OYz9CdGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStAaiBnSmIlRlVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=8hS0xg==; SMSError=; authError=; cfidsgib-w-mvideo=w1UINpPhTtJuTblhPH3ZMTAbyibO1mxLbpNJL0XWEvLhmugCupypbTfTsfwNm0+eR2x/2TTxy2oma1OxNQkoS5fOP2nGuq5uiLEtoOlA/6VdrHvPnhGtOnO7jOWXhgPx7hAQ8NOjHoK6letjf4dDOePbJzHQfu7t22kx; cfidsgib-w-mvideo=w1UINpPhTtJuTblhPH3ZMTAbyibO1mxLbpNJL0XWEvLhmugCupypbTfTsfwNm0+eR2x/2TTxy2oma1OxNQkoS5fOP2nGuq5uiLEtoOlA/6VdrHvPnhGtOnO7jOWXhgPx7hAQ8NOjHoK6letjf4dDOePbJzHQfu7t22kx; gsscgib-w-mvideo=Prpw+lnkZslgeoPXJwohlyrzMvKEzYeHSP1Rr5q2dUmbzCvBbQPA+kYRo24OeSeudbY/fybK6iIYkqfUhUu9EFfV/SqIY27T1vOl8VMOTtPbCCJYVA2+NdS5kItfs5z/muW24C6ldDfbrR5SuJJDG46abwW+mdAlEdzhS6r6Un6wrTJeA99TLfeowJT5SEUR7Al5yqzKwE1hzN7stNZ35wsJ+TLHfdxKMFwjMiU0fudUWhmcNPNexoA9dT3nMw==; gsscgib-w-mvideo=Prpw+lnkZslgeoPXJwohlyrzMvKEzYeHSP1Rr5q2dUmbzCvBbQPA+kYRo24OeSeudbY/fybK6iIYkqfUhUu9EFfV/SqIY27T1vOl8VMOTtPbCCJYVA2+NdS5kItfs5z/muW24C6ldDfbrR5SuJJDG46abwW+mdAlEdzhS6r6Un6wrTJeA99TLfeowJT5SEUR7Al5yqzKwE1hzN7stNZ35wsJ+TLHfdxKMFwjMiU0fudUWhmcNPNexoA9dT3nMw==; _dc_gtm_UA-1873769-37=1; fgsscgib-w-mvideo=1VNFa0d3a84c7cb327bb095aad8c981621a99731; fgsscgib-w-mvideo=1VNFa0d3a84c7cb327bb095aad8c981621a99731; cfidsgib-w-mvideo=rkeSyPxtiySrgelzKzPM6CINhkMK8zlpbgt9HvLx04xgT4xXf1fom/0uGj5QuVrem67HB+7MLXbdBmfO06lBVjxmVK1GsUVC0Q/x0CRI2lF9H9z7vH+DC3usUUZJuPoe7w6YIcmxXU7l6IG/V4SUwPH8maxncTZz/US8; CACHE_INDICATOR=false; _sp_id.d61c=f5d929a1-3eb4-453c-91ba-79c13731c80f.1662388356.2.1662553844.1662388356.ba144132-79cd-4ee2-9ac4-73ab28923e9b.9e0a970d-6f69-4095-bae0-32eac316caa0.113b02fc-eb2a-42a4-aed8-93e51d0841a2.1662553835395.3; _ga=GA1.2.1028379010.1662388356; tmr_detect=0%7C1662553852846; tmr_reqNum=65; _ga_CFMZTSS5FM=GS1.1.1662553838.2.1.1662553874.0.0.0; _ga_BNX5WPP3YK=GS1.1.1662553838.2.1.1662553874.24.0.0; MVID_ENVCLOUD=prod1',
    'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914/tolko-v-nalichii=da/vstroennaya-pamyat=256gb/collection_top=iphone-13-pro---13-pro-max',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '8e66cbf3dbf942878d2efa1bcfae6d04-9adf23a1e147b97a-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-set-application-id': '48054df3-2c3c-4d56-9813-60dbd0293c60',
}

params = {
    'productIds': '30063191,30063591,30063588,30063590,30063589,30063594,400007541,400007535,400007561,400007550',
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}

response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

product_prices = response.get('body').get('materialPrices')
for prices in product_prices:
    product_id = prices['price']['productId']
    base_price = f"Базовая стоимость: {prices['price']['basePrice']}\n"
    sale_price = f"Стоимость со скидкой: {prices['price']['salePrice']}\n"
    promo_price = f"Промо цена: {prices['price']['basePromoPrice']}\n"
    try:
        result[product_id] += [base_price, sale_price, promo_price]
    except:
        pass

result_string = ''

for r in result:
    result_string += f"{' '.join(result[r])}\n"


# 66784444 - polina
bot = telebot.TeleBot('5407256392:AAFCjQB0jtUcV1KEZ75Hm11PJcn79SYkhgU')

bot.send_message(66784444, f"М-Видео\n"
                           f"\n"
                           f"{result_string}")
bot.send_message(198384562, f"М-Видео\n"
                            f"\n"
                           f"{result_string}")
