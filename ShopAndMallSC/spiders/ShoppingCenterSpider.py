import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from datetime import date
import logging
from ..items import ShopandmallscItem

class ShoppingCenterSpider(CrawlSpider):
    name = 'ShoppingCenterSpider'
    allowed_domains = ['shopandmall.ru']
    start_urls = ['https://shopandmall.ru/torgovye-centry/'+str(i) for i in range(86)]
    rules = (
    Rule(LinkExtractor(allow=(r'torgovye-centry/d{:2}',),
                       deny='catalog'),
                       follow=True),

    Rule(LinkExtractor(restrict_xpaths="//div[@class='header-in-list']"),
                       callback='parse_item',
                       follow=False)
    )

    def parse_item(self, response):
        item = ShopandmallscItem()
        url = response.request.url

        info = response.css('div.overlay-info-block').extract_first()
        if info is not None:
            try:
                name = re.search(r'</p>(.*?)</div>', str(info)).group(1)
            except:
                name = None
            try:
                gla = re.search(r'</span>(.*?)<sup>', str(info)).group(1).split(' ')[0]
            except:
                gla = None
            try:
                city = response.css('div.overlay-info-block a::text').extract_first()
            except:
                city = None
        else:
            info = response.css('div.l-col-1-i').extract_first()
            if info is not None:
                try:
                    name = name = re.search(r'"name">(.*?)</p>', str(info)).group(1)
                except:
                    name = None
                try:
                    gla = re.search(r'Сдаваемая в аренду площадь здания:</div><div class="i-view"><p>(.*?)<sup>', str(info)).group(1).split(' ')[0]
                except:
                    gla = None
                try:
                    city = re.search(r'>(.*?)</a></p></div></li>', str(info)).group(1).split('>')[-1]
                except:
                    city = None

        item['date'] = str(date.today())
        item['name'] = name
        item['gla'] = gla
        item['city'] = city
        item['url'] = url

        return item
