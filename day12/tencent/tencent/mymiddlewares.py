from scrapy.exceptions import  IgnoreRequest
from selenium import webdriver
from scrapy.http import HtmlResponse

class tencentdownload(object):

    def __init__(self):
        pass

    def process_request(self, request, spider):
        '''
        实现自定义下载就可以了
        :param request:
        :param spider:
        :return:
        '''
        # print('in mymiddlewares!')
        driver = webdriver.PhantomJS()
        driver.get(request.url)
        # 等待
        # 隐式等待十秒
        driver.implicitly_wait(10)
        # 获取页面内容
        html_str = driver.page_source

        return HtmlResponse(url=request.url,body=html_str,encoding='utf-8',request=request)
