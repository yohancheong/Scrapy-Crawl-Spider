from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class WikiSpider(CrawlSpider):

    name = 'wikipedia'
    allowed_domains = ['wikipedia.org']
    start_urls = ["https://en.wikipedia.org/wiki/Mathmetics",]

    rules = (
        Rule(LinkExtractor(allow="https://en.wikipedia.org/wiki/", restrict_xpaths="//div[@class='mw-body']//a"), callback='parse_page', follow=False),
    )

    def parse_page(self, response):        
        print response.xpath('//h1[@class="firstHeading"]/text()').extract()
        return