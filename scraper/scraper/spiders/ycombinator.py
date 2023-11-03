import scrapy


class YcombinatorSpider(scrapy.Spider):
    # Default generated by cmd genspider ycombinator news.ycombinator.com
    # name = "ycombinator"
    # allowed_domains = ["news.ycombinator.com"]
    # start_urls = ["https://news.ycombinator.com"]

    # def parse(self, response):
    #     pass
    name = "ycombinator"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com/"]
 
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4690.0 Safari/537.36'  # Replace with the desired User-Agent value
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)
 
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        for el in soup.select(".athing"):
            obj = {}
            try:
                obj["titles"] = el.select_one(".titleline > a").text
            except:
                obj["titles"] = None
            yield obj
 
 
 
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
 
    process = CrawlerProcess()
    process.crawl(AmazonSpider)
    process.start()