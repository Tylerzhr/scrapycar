import string
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import parse_qs, urlencode, urlparse
from scrapycar.items import CarBrandItem

class AutomobileSpider(scrapy.Spider):
    name = "automobile"
    allowed_domains = ["www.autohome.com.cn"]
    #获取http://www.autohome.com.cn/grade/carhtml/C.html按拼音搜索车品牌界面
    def start_requests(self):
        #不存在的车系开头
        for x in string.ascii_uppercase:
            if x not in "EIUV":
                url = "http://www.autohome.com.cn/grade/carhtml/" + x + ".html"
                yield Request(url,self.get_brand,meta={'pinyin': x})
    #start_urls = [
    #    "http://www.autohome.com.cn/grade/carhtml/" + x + ".html"
        #不存在的车系开头
    #    for x in string.ascii_uppercase if x not in "EIUV"
    #]

    #需要处理的链接，满足条件调用parse_item的过滤器
    # rules = (
    #     Rule(LinkExtractor(allow=("/\d+/#",)), callback="parse_item"),
    # )
    def get_brand(self,response):
        #第零位链接list型，第一位存放拼音，第二位存放brand，第三位存放logo
        # #车型链接//li/h4/a
        # car_type_urls=response.xpath("//li/h4/a/@href").extract()
        # #车型名称//li/h4/a/text()
        # #car_type_name=response.xpath("//li/h4/a/text()").extract()
        # # 车辆品牌"//dl/dt/div/a/text()"
        # car_brand_name=response.xpath("//dl/dt/div/a/text()").extract()
        # #print(car_brand_name)
        # #车辆首字母response.meta["pinyin"]
        # #print("链接 "+format(car_type_urls)+"车型名称："+format(car_type_name))
        # #车辆品牌图标
        # pinyin = response.meta["pinyin"]
        #car_brand_imagUrl = response.xpath("//dt/a/img/@src").extract()
        item=CarBrandItem()
        dls = response.xpath("//dl")
        for dl in dls:
            #car_brand_imagUrl = dl.xpath("./dt/a/img/@src").extract()
            #car_type_urls=dl.xpath("./dd/ul/li/h4/a/@href").extract()
            pinyin=response.meta["pinyin"]
            car_brand_name=format(dl.xpath("./dt/div/a/text()").extract()).replace("['", '').replace("']", '')
            car_type_name = dl.xpath("./dd/ul/li/h4/a/text()").extract()
            item['carbrand']=car_brand_name
            item['pinyin']=pinyin
            for type in car_type_name:
                item['cartype'] = type
            #item['logo']=car_brand_imagUrl
            #print(item['logo'])
            # for url in car_type_urls:
            #     yield Request(url,callback=self.get_item,meta={"car_brand_name":car_brand_name})
                yield item
            #print( "车牌名称：" + format(car_brand_name)+"首拼音   "+pinyin+"logo"+car_brand_imagUrl)

    # def parse(self,response):
    #     params = {
    #         "url": response.url,
    #         "status": response.status,
    #         "headers": response.headers,
    #         "body": response.body,
    #     }
    #
    #     response = HtmlResponse(**params)
    #
    #     return super().parse(response)

    def get_item(self, response):
        item=CartypeItem()
        #获取上一请求的所有数据
        sel = response.css("div.path")
        car_brand_name = format(response.meta["car_brand_name"])
        car_type_name= format(sel.css("a:last-child::text").extract())

        for sel1 in response.css("div.interval01-list-cars-infor"):
            #item['model']=sel1.css("a::text")[0]
            car_model=format(sel1.css("a::text")[0].extract())
            #print("车品牌："+car_brand_name+"车系列"+car_type_name+"车型"+car_model)
            item['model']=car_model
            item['carbrand']=car_brand_name
            item['cartype']=car_type_name
            # print(item['cartype'],item['carbrand'],item['model'])
            return item

    #def stop_sale(self, response):
        #qs = parse_qs(urlparse(response.url).query)

        #body = json.loads(response.body_as_unicode())

        #for spec in body["Spec"]:
            #yield {
                #"model_id": str(spec["Id"]),
                #"model_name": str(spec["Name"]),
                #"series_id": str(qs["s"][0]),
           # }