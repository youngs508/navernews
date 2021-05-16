# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItems



class NewsSpider(CrawlSpider):
    
    name = 'test13'
    allowed_domains = ['news.naver.com']
    start_urls = ['https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20210516']

    # 링크 크롤링 규칙 (정규 표현식 사용 추천)
    # page=\d$ : 1자리 수
    # page=\d+ : 제한 없음, follow=True
    rules = [
        Rule(LinkExtractor(allow=r'&page=\d+'), callback='parse_parent', follow=True),
    ]

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)

        for url in response.css('div.list_body.newsflash_body > ul.type06_headline'):
            # URL 신문 기사 URL
            article_url = url.css('li > dl > dt:nth-child(2) > a::attr(href)').extract_first().strip()
            # 요청
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url})
            
    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        self.logger.info('--------------------------------------')
        self.logger.info('Response From Parent URL : %s' % response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('--------------------------------------')

        # 헤드라인
        headline = response.css('h3#articleTitle::text').get().strip()
        # 본문
        c_list = response.css('div#articleBody > div::text').getall()
        contents = ''.join(c_list).strip()

        yield ArticleItems(headline=headline, contents=contents, 
            parent_link=response.meta['parent_url'], article_link=response.url)





       
