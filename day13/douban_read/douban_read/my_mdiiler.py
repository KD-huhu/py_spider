from selenium import webdriver
from scrapy.http import HtmlResponse


class MyMiddlerWares(object):
    def __init__(self):
        pass

    def process_request(self,request,spider):
        # print(1)
        '''
        默认使用selenium
        用下载器下载的请求，meta={flag:True}
        '''

        if not request.meta['flag']:
            # print('selenium')
            '''
            用selenium
            '''
            driver = webdriver.Chrome()
            driver.get(request.url)
            driver.implicitly_wait(20)
            html_str = driver.page_source
            driver.quit()
            return HtmlResponse(url=request.url,body=html_str,encoding='utf-8',request=request)
        #return None 表示用下载器下载。
        return None