import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARN)


class KeySpider(scrapy.Spider):
    name = 'keyforge_spider'
    start_urls = ['https://keyforge-compendium.com/cards']

    def parse(self, response):
        links = response.css(
            'div.kfc__cardlist__card.kfc-card > a ::attr(href)')
        for l in links:
            yield response.follow(url=l, callback=self.parse_cards)

    def parse_cards(self, response):
        for e in response.css('div.kfc__card__info > ul'):
            yield {
                'title': response.css('h1 ::text').get().strip(),
                'properties': e.css('li ::text').getall()
            }
