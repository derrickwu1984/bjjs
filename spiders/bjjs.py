# -*- coding: utf-8 -*-
import scrapy,logging
from scrapy.loader import  ItemLoader
from bjjs.items import BjjsItem

class BjjsSpider(scrapy.Spider):
    name = 'bjjs'
    allowed_domains = ['http://www.bjjs.gov.cn/eportal/ui?pageId=308900']
    start_urls = ['http://www.bjjs.gov.cn/eportal/ui?pageId=308900/']
    crawl_url="http://www.bjjs.gov.cn/eportal/ui?pageId=308900"
    def start_requests(self):
        for i in range(1,749):
            data=self.pre_data(i)
            logging.warning(i)
            yield scrapy.FormRequest(url=self.crawl_url,formdata=data,method="POST",callback=self.parse)
        pass
    def pre_data(self,curretnPage):
        data = {
            "filter_LIKE_QYMC":"",
            "filter_LIKE_AQSCXKZBH": "",
            "filter_LIKE_ZYFZR": "",
            "currentPage": str(curretnPage),
            "pageSize":"15",
            "OrderByField":"",
            "OrderByDesc":""
        }
        return data
    def parse(self, response):
        all_msg = response.xpath("//table[@class='gridview']/tbody/tr")
        for msg in all_msg[1:]:
            # "."选取当前节点，xpath不加点就会从根开始查询。
            tr_info = msg.xpath(".//td//text()").extract()
            BjjsItemLoader = ItemLoader(item=BjjsItem(), response=response)
            BjjsItemLoader.add_value("cert_no",tr_info[1])
            BjjsItemLoader.add_value("corp_name", tr_info[2])
            BjjsItemLoader.add_value("corp_repr", tr_info[3])
            BjjsItemLoader.add_value("admi_code", tr_info[4])
            BjjsItemLoader.add_value("regi_addr", tr_info[5])
            BjjsItemLoader.add_value("econ_type", tr_info[6])
            BjjsItemLoader.add_value("prom_rang", tr_info[7])
            BjjsItemLoader.add_value("prom_cell", tr_info[8])
            BjjsItemLoader.add_value("chek_date", tr_info[9])
            BjjsItemLoader.add_value("last_chek", tr_info[10])
            BjjsItemLoader.add_value("post_chek", tr_info[11])
            bjjsInfo =BjjsItemLoader.load_item()
            yield bjjsInfo
                # print(cert_no, corp_name, corp_repr, admi_code, regi_addr, econ_type, prom_rang, prom_cell, chek_date,
            #       last_chek, post_chek)