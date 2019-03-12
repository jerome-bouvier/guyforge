import scrapy
import logging

# logging.getLogger('scrapy').setLevel(logging.WARNING)


class KeySpider(scrapy.Spider):
    name = 'keyforge'
    start_urls = 'https://keyforge-compendium.com/cards'

    def parse(self, response):
        links = response.css(
            'body:nth-child(2) main.kfc section.kfc__cardlist div.kfc__cardlist__card.kfc-card:nth-child(1) > a:nth-child(1) ::text')
        for l in links:
            yield response.follow(url=l, callback=self.parse_cards)

    def parse_cards(self, response):
        yield {'title': response.css(
            'h1 ::text').extract_first().strip(),
            'text': response.css(
            'div.kfc__card__info > ul > li ::text').extract_first().strip(),
            'type': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(1) ::text').extract_first().strip(),
            'house': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(3) ::text').extract_first().strip(),
            'rarity': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(5) ::text').extract_first().strip(),
            'artist': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(6) ::text').extract_first().strip(),
            'number': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(8) ::text').extract_first().strip(),
            'set': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(9) ::text').extract_first().strip(),
            'In Decks': response.css(
            'main.kfc div.kfc__card div.kfc__card__info ul:nth-child(1) > li:nth-child(10) ::text').extract_first().strip()
        }
