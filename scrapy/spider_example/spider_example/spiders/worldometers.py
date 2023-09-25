import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        
        countries_list = response.xpath('//td/a')

        for country in countries_list:
            country_name = country.xpath('./text()').get()
            country_link = country.xpath('./@href').get()

            # open absolute url
            # absolute_url = response.urljoin(country_link)
            # yield scrapy.Request(url=absolute_url, callback=self.parse_country, meta={'country': country_name})

            # open relative url
            yield response.follow(url=country_link, callback=self.parse_country, meta={'country': country_name})

    
    def parse_country(self, response):
        country_name = response.request.meta['country']
        
        population_years = response.xpath('(//table[contains(@class, "table")])[1]/tbody/tr')

        for item in population_years:
            year = item.xpath('./td[1]/text()').get()
            population = item.xpath('./td[2]/strong/text()').get()

            yield {
                'country': country_name,
                'year': year,
                'population': population,
            }
