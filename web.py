import requests
import bs4
from bs4 import BeautifulSoup

url = 'https://pingi.co/'

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')


class PingiScrapper:

    def symbol(self):
        symbols_list = list()
        cryptoes = content.select('span.english-content-product.coin-symbol')
        for crypto in cryptoes:
            index = -1
            for span in crypto:
                index += 1
                if index == 2:
                    symbols_list.append(span.strip())
        return symbols_list

    def price(self, crypto):
        value = crypto + '_IRT'
        target_tag = 'tr'
        key = "data-table-coin-prices"
        crypto_tag = content.findAll(target_tag, {key: value})
        for cryp in crypto_tag:
            index_tag = -1
            for tag in cryp:
                if index_tag == 2:
                    for div in tag:
                        for span in div:
                            for price in span:
                                if type(price) == bs4.element.NavigableString:
                                    price = price.strip()
                                    return price
                index_tag += 1


def coins():
    scrapper = PingiScrapper()
    symbols = scrapper.symbol()
    coins_list = dict()
    for sym in symbols:
        price = scrapper.price(sym)
        coins_list[sym] = price + ' تومان'
    print(coins_list)
    return coins_list


coins()