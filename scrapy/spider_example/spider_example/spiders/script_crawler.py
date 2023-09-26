import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScriptCrawlerSpider(CrawlSpider):
    name = "script_crawler"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies_letter-X"]

    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),) # Allow list of url
    # rules = (Rule(LinkExtractor(deny=r"Items/"), callback="parse_item", follow=True),) # Deny list of url

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//ul[@class="scripts-list"]/a')), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths=('(//a[@rel="next"])[1]'))),
             ) # Allow matching with xpath

    def parse_item(self, response):
        article_item = response.xpath('//article[@class="main-article"]')

        print(response.url)

        yield {
            'name': article_item.xpath('./h1/text()').get(),
            'plot': article_item.xpath('./p/text()').get(),
        }
