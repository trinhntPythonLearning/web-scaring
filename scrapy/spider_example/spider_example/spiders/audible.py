import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search/"]

    def parse(self, response):
        item_list = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for item in item_list:
            title = item.xpath('.//li/h3[contains(@class, "bc-heading")]/a/text()').get()
            author = item.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').get()
            length = item.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                'title': title,
                'author': author,
                'length': length,
            }
        
        next_page_url = response.xpath('//ul[contains(@class, "pagingElements")]//span[contains(@class, "nextButton")]/a/@href').get()
        print(next_page_url)

        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)
