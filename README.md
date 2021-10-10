# CoinNewsScraper
Scraper for crypto-currency news
To install you need to download the files in this repository and open them through the command line. For example: Python main.py
Also you will need to install requests and beatifulSoup library.
Use:
pip install bs4
pip install requests
Then you can import class in your document and use. For example: 
from coin_market_news import news_scraper
from coin_overview import overview_scraper

if __name__ == "__main__":
    coinScraper = news_scraper()
    overviewScraper = overview_scraper()
    
 Then you can use methods.
  ScrapOverview('Name of the currency') - will display overview of the currency.
  find_coin_news('Name of the currency') - Will show latest news about the currency.
  ScrapTheLink(Number in the order of news list) - will show all <p> tags in the choosen news link.
Example:
if __name__ == "__main__":
    coinScraper = news_scraper()
    overviewScraper = overview_scraper()
# scraps the overview of the coin
    overviewScraper.ScrapOverview('cardano')
# scraps the news 
    coinScraper.find_coin_news('cardano')

# scraps the p tags in choosen news 1-10
    coinScraper.ScrapTheLink(5)
