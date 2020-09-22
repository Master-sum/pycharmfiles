import scrapy
class Aritcl(scrapy.Spider):
    name = "aritcl"

    def start_requests(self):
        urls = [
            'https://www.baidu.com/',
            'https://www.jianshu.com/p/1ad2745709cc'
        ]
        return [scrapy.Request(url=url,callback=self.t) for url in urls]

    def t(self,response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print(title)