from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScriptCrawlerSpider(CrawlSpider):
    name = "script_crawler"
    allowed_domains = ["subslikescript.com"]
    # start_urls = ["https://subslikescript.com/movies_letter-X"]

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'

    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/movies_letter-X',
                             headers={'user-agent': self.user_agent})

    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),) # Allow list of url
    # rules = (Rule(LinkExtractor(deny=r"Items/"), callback="parse_item", follow=True),) # Deny list of url

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//ul[@class="scripts-list"]/a')), callback="parse_item", follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths=('(//a[@rel="next"])[1]')), process_request='set_user_agent'),
             ) # Allow matching with xpath
    
        # Setting the user-agent
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        article_item = response.xpath('//article[@class="main-article"]')

        print(response.url)

        yield {
            'name': article_item.xpath('./h1/text()').get(),
            'plot': article_item.xpath('./p/text()').get(),
            'user-agent': response.request.headers['User-Agent']
        }
