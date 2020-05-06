import time
from queue import Queue
from selenium import webdriver
from lxml import etree
import threading

'''
生产者生产每一页的html页面，也就是生产者负责请求---class Producter
消费者消费html，解析---class Consumer
缓冲区：队列来做
'''


class Producter(threading.Thread):
    def __init__(self,url,queue_page,name):
        super().__init__()
        self.queue_page = queue_page
        self.name = name
        self.url = url

    def run(self):
        while True:
            if self.queue_page.empty():
                break
            # 获取页码
            page = self.queue_page.get()
            html_str = self.get_html(page)
            print('=========producter第{}页============@{}'.format(page,self.name))
            # 将生产数据放入公共缓冲队列
            queue_html.put((page,html_str))

    def get_html(self,i):
        '''
        获取一页页面内容
        :param i:页码
        :return:页面的字符串内容
        '''
        driver = webdriver.PhantomJS()
        driver.get(self.url.format(i))
        return driver.page_source


class Consumer(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        while True:
            # 保证生产者都生产完了，同时缓冲区没东西，消费者才停止消费
            if queue_html.empty() and flag:
                break
            try:
                page,html_str = queue_html.get(block=False)
                self.parse_html(html_str)
                print('保存第{}页成功！@{}'.format(page, self.name))
            except Exception:
                pass

    def parse_html(self,html_str):
        tree = etree.HTML(html_str)
        div_list = tree.xpath('//div[@class="recruit-list"]')

        for div in div_list:
            ##提取
            title = div.xpath('./a/h4/text()')[0]
            type = div.xpath('./a/p/span[1]/text()')
            place = div.xpath('./a/p/span[2]/text()')
            class_job = div.xpath('./a/p/span[3]/text()')
            time1 = div.xpath('./a/p/span[4]/text()')
            responsibility = div.xpath('.//p[@class="recruit-text"]/text()')
            item = {}
            item['title'] = title
            item['type'] = type
            item['place'] = place
            item['class_job'] = class_job
            item['time1'] = time1
            item['responsibility'] = responsibility
            # print(title)


if __name__ == '__main__':
    start = time.time()
    # 1、创建一个队列：公共缓冲区
    queue_html = Queue()
    '''
    1、创建一个队列：公共缓冲区
    '''
    # 轮询参数
    # 表示生产者没有生产完成
    flag = False
    # 先将生产者类改成线程类
    # 1.创建p的任务队列
    queue_page = Queue()
    # 初始化
    for i in range(10):
        queue_page.put(i)
    base_url = 'https://careers.tencent.com/search.html?index={}&keyword=python'
    crawl_list_p = ['aa', 'bb', 'cc']
    p_threads = []
    for crawl in crawl_list_p:
        t = Producter(base_url,queue_page,crawl)
        t.start()
        p_threads.append(t)

    # 创建四个线程消费
    crawl_list_c = ['11', '22', '33', '44']
    for crawl in crawl_list_c:
        t = Consumer(crawl)
        t.start()

    # 将生产者都加入阻塞join()
    for p in p_threads:
        p.join()
    flag = True
    print('程序执行的时间：', time.time() - start)
    # 程序执行的时间： 30.4002366065979