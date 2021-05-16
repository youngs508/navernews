# Scrapy settings for section05_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'section05_3'

SPIDER_MODULES = ['section05_3.spiders']
NEWSPIDER_MODULE = 'section05_3.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 다운로드 간격
DOWNLOAD_DELAY = 1

# 쿠키 사용
COOKIE_ENABLED = True

# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
  'Referer': 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20210514&page=2',
}

# 파이프라인 활성화
# 숫자가 작을 수록 우선순위 상위
ITEM_PIPELINES = {
  'section05_3.pipelines.NewsSpiderPipeline': 300,
}

# User-agent 미들웨어 사용
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글 쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'

# 캐시 사용
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
