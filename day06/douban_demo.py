from selenium import webdriver
# 导入显示等待模块
from selenium.webdriver.support.wait import WebDriverWait
# 导入定位器模块
# 包含seleniunm内置一些条件
from selenium.webdriver.support import expected_conditions as EC
# 导入定位器的定位方法模块
from selenium.webdriver.common.by import By
from lxml import etree


class DoubanSpider(object):

    def __init__(self,url):
        # 读入url
        self.url = url
        # 创建浏览器驱动
        self.driver = webdriver.Chrome()
        # 调用主程序
        self.main()


    def get_html(self,url):
        # 请求url
        self.driver.get(url)
        # 等待请求结束
        # 使用显示等待的方法：可以聚焦到页面中特定元素出现就等待结束。
        # 使用显示等待步骤
        # （1）、创建等待对象
        wait = WebDriverWait(self.driver,20)
        # driver:表示这个等待对象监听到那个驱动浏览器程序上
        # 20：显示等待的最大等待时长，20秒还没等待到特定元素加载出来，就报一个超时异常
        # （2）用wait对象来进行条件判断
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[1]/div[3]/div/div/div[3]')))
        '''
        EC.presence_of_element_located(定位器)
        监控定位器
        定位器是一个元组
        所以：EC.presence_of_element_located（（By.定位器定位方法 + 具体定位的属性））
        '''
        # 获取页面内容
        # 返回浏览器得到的页面资源
        return self.driver.page_source


    def pares_div(self,div_list):
        for div in div_list:
            try:
                book_name = div.xpath('.//div[@class="title"]/a/text()')[0]
                print(book_name)
            except Exception:
                pass
        pass


    def main(self):
        # 分页请求
        # 通过观察发现豆瓣图书搜索的页码并不是确定的，所以使用 for 循环难以实现
        # 在本案例中使用 while 循环来实现分页爬取
        i = 0
        while True:
            # 获取页面信息
            html_page = self.get_html(self.url % (i * 15))
            # 测试
            # print(html_page)
            # 将html页面转换为json格式
            json_data = etree.HTML(html_page)
            # 获取数据
            div_list = json_data.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[position()>1]')
            # 测试
            # print(div_list)
            # 判断获得的div_list是不是空
            # 当div_list为空时，跳出循环
            if not div_list:
                break
            # 提取数据
            self.pares_div(div_list)
            i += 15
            # break


if __name__ == '__main__':
    base_url = 'https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=%s'
    book_list = []
    DoubanSpider(base_url)