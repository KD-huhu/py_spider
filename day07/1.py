import time,os
from selenium import webdriver
from lxml import etree
from excel_utils2.test import ExcelUtils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC#seleniunm内置一些条件
from selenium.webdriver.common.by import By
import requests

class DoubanReader(object):


    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.filename = '豆瓣python书籍.xls'
        self.main()


    def get_xpath(self,url):
        #准备参数
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        return response.text

    def get_content_by_selenium(self,url):
        #1,创建驱动
        # driver = webdriver.PhantomJS()

        #2请求url
        self.driver.get(url)
        #3、等待
        #强制等待:弊端：死板，而且有的时候还可能等待不够，造成数据的缺失
        # time.sleep(3)
        #隐式等待：相当于页面在等待到转圈圈结束，页面完全加载出来位置。
        #弊端：等待的还是太久了。
        # driver.implicitly_wait(10)#10秒钟还没有全部加载完成的话，就会报超时异常
        #显示等待：可以聚焦到页面中特定元素出现就等待结束。
        # 使用显示等待步骤
        #（1）、创建等待对象
        # 20：显示等待的最大等待时长，20秒还没等待到特定元素加载出来，就报一个超时异常
        #driver:表示这个等待对象监听到那个驱动浏览器程序上
        wait = WebDriverWait(self.driver,20)
        # （2）用wait对象来进行条件判断
        '''
        EC.presence_of_element_located(定位器)
        定位器是一个元祖(用什么定位器：id,xpath,css,'对应的选择器的语法')
        '''
        wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="root"]')))#等到啥时候为止
        #4、获取页面内容
        return self.driver.page_source

    def parse_div(self,div_list):
        '''
        解析每个div，获取书籍
        :param div_list:
        :return:
        '''
        #存储每一页的数据
        info_list = []
        for div in  div_list:
            #异常发生程序终止---当前线程中止
            #规则：异常必须要处理。
            #异常时层层抛出的,所以在处理异常的时候，一定要分析好处理的位置，
            # 这样决定了你是否能利用异常做一些程序的附加功能
            #异常功能：
            try:
                #书籍名称
                book_title = div.xpath('.//div[@class="title"]/a/text()')[0]
                # print(book_title)
                info = div.xpath('.//div[@class="meta abstract"]/text()')
                # print(info)
                infos = info[0].split(r'/')
                # print(infos)
                #在爬取数据的时候，分析网站，提取数据的时候，有时候总有特例
                #作者
                book_actor = infos[0]
                #出版社
                book_publish = infos[-3]
                #价格
                book_price = infos[-1]
                #出版日期
                book_date = infos[-2]
                #详情页链接
                detail_url = div.xpath('.//div[@class="item-root"]/a/@href')[0]
                item = {}
                item['book_title']  = book_title
                item['book_actor']  = book_actor
                item['book_price']  = book_price
                item['book_publish']  = book_publish
                item['detail_url']  = detail_url
                # print(item)
                info_list.append(item)
            except Exception:
                pass
        if os.path.exists(self.filename):
            ExcelUtils.write_to_excel_append(self.filename,info_list)
        else:
            ExcelUtils.write_to_excel(self.filename,'python书籍',info_list)

    def main(self):
        #分页请求
        # for i in range(1):
        i = 0
        while True:
            html_str = self.get_content_by_selenium(self.url %(i*15))
            # print(html_str)
            #页面内容转成element对象就可以使用xpath语法来进行获取页面内容
            html = etree.HTML(html_str)
            #获取
            div_list = html.xpath('//div[@id="root"]/div/div[2]/div/div/div[position()>1]')
            # print(div_list)
            if not div_list:
                break
            self.parse_div(div_list)
            i+=1

if __name__ == '__main__':
    #基础url
    base_url = 'https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=%s'
    DoubanReader(base_url)
