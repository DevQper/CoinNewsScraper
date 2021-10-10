from coin_market_news import news_scraper
from coin_overview import overview_scraper

if __name__ == "__main__":
    coinScraper = news_scraper()
    overviewScraper = overview_scraper()
# scraps the overview of the coin
    overviewScraper.ScrapOverview('cardano')
# scraps the news 
    coinScraper.find_coin_news('cardano')

# scraps the p tags in choosen news 1-10
    coinScraper.ScrapTheLink(5)