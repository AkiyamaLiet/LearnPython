#-*- coding:utf=8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    #def start_requests(self):
        #urls = [
            #'http://quotes.toscrape.com/page/1/',
            #'http://quotes.toscrape.com/page/2/',
        #]
        #for url in urls:
            #yield scrapy.Request(url=url, callback=self.parse)
        #callback是回调函数，即对每个请求都进行这个函数的操作
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]        
    # 可以直接用start_urls创建一个初始url列表，这个列表会默认实现start_requests()方法来创建SPider初始化的请求
        
    #def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log('Saved file %s' % filename)
        
    # 文件写入的操作
        
        
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
        
        next_page = response.css('li.next a::attr(href)').extract_first()
        #if next_page is not None:
            #next_page = response.urljoin(next_page)
            #yield scrapy.Request(next_page, callback=self.parse)
            
        # response.urljoin会自动检测最先的域名地址，即 'http://quotes.toscrape.com/page/1/' 中
        # response.urljoin时 基地址会自动识别为 'http://quotes.toscrape.com/' 并在后面加上 .urljoin() 括号中的内容，十分方便            

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        
        # 使用 response.follow()可以支持自动关联URLS,不需要使用 urljoin
        
        #for href in response.css('li.next a::attr(href)'):
        #    yield response.follow(href, callback=self.parse)    
        
        # response.follow也可以自动解析 href标签
        
        
        #for a in response.css('li.next a'):
        #    yield response.follow(a, callback=self.parse)        
        
        # 即使是直接的一个href元素也可以
