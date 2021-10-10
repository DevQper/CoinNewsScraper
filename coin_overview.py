from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests

class overview_scraper():


    def ScrapOverview(self, query):
        
        url = 'https://coinmarketcap.com/currencies/' + query +'/'
        # url_news = 'https://coinmarketcap.com/currencies/cardano/news/'


        # print(url)
        page = requests.get(url)
        # news_page = requests.get(url_news)
        currency_parser = BeautifulSoup(page.content, 'html.parser')
        # news_parser = BeautifulSoup(news_page.content, 'html.parser')

        page_currency_title = currency_parser.find("div", class_ = "sc-16r8icm-0 gpRPnR nameHeader").find("h2")
        page_currency_price = currency_parser.find("div", class_ = "imn55z-0 hCqbVS price").find("div")
        page_currency_overview_title = currency_parser.find("h2", class_ = "sc-1q9q90x-0 jCInrl")
        page_currency_overview = currency_parser.find("div", class_ = "sc-16r8icm-0 kjciSH contentClosed hasShadow").find("p")


        print(page_currency_title.text)

        print(page_currency_price.text)

        print(page_currency_overview_title.text + ":")

        print(page_currency_overview.text)

