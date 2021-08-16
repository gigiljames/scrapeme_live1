import scrapy
from ..items import ScrapemeLiveItem

class Scrapeme1Spider(scrapy.Spider):
    name = 'scrapeme1'
    #allowed_domains = ['https://scrapeme.live/shop/']
    start_urls = ['https://scrapeme.live/shop//']

    def parse(self, response):
        items = ScrapemeLiveItem()
        html_response = response.xpath('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]')
        for i in html_response:
            name = i.xpath('h2/text()').extract()
            price = i.xpath('span[@class="price"]/span/text()').extract()
            url = i.xpath('@href').extract()
            items['name'] = ''.join(name)
            items['price'] = ''.join(price)
            items['url'] = ''.join(url)
            yield items