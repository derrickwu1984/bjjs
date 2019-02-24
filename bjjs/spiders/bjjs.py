# -*- coding: utf-8 -*-
import scrapy,logging


class BjjsSpider(scrapy.Spider):
    name = 'bjjs'
    allowed_domains = ['http://www.bjjs.gov.cn/eportal/ui?pageId=308900']
    start_urls = ['http://www.bjjs.gov.cn/eportal/ui?pageId=308900/']
    def start_requests(self):
        for i in range(2):
            data=self.pre_data(i)
            yield scrapy.FormRequest(url=self.start_urls, formdata=data, method="POST",  callback=self.parse,)
        pass
    def pre_data(self,curretnPage):
        data = {
            # "pageId": "308900",
            "filter_LIKE_QYMC":"",
            "filter_LIKE_AQSCXKZBH": "",
            "filter_LIKE_ZYFZR": "",
            "currentPage": curretnPage,
            "pageSize":"15",
            "OrderByField":"",
            "OrderByDesc":""
        }
        return data
    def parse(self, response):
        logging.warning(response.body)
        pass
