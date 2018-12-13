class UsProxySpider(scrapy.Spider):
    name = 'us_proxy'

    def start_requests(self):
        url = 'https://us-proxy.org'
        yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait': 0.5})

    def parse(self, response):
        for tr in response.xpath("//table[@id='proxylisttable']/tbody/tr"):
            yield {
                'ip': tr.xpath(".//td[1]/text()"),
                'port': tr.xpath(".//td[2]/text()")
            }
