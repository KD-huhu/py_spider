from selenium import webdriver
from lxml import etree
import threading
import time
from queue import Queue
class Tencent(threading.Thread):
    def __init__(self,url,queue_page,name):
        #初始化父类中参数
        super().__init__()
        self.queue_page = queue_page
        self.name = name
        self.url = url
        # self.parse()


    def run(self):
        # self.parse()
        #一个类就相当于一个线程
        #四个线程干20个任务，只能每个线程做多件事
        #重复不断的取做：从【队列】中取出一个页码，爬取，解析
        while True:
            # 一定要先做跳出循环的条件准备
            if self.queue_page.empty():
                break
            #取页码
            page = self.queue_page.get()
            print('===============第{}================@{}'.format(page,self.name))
            #请求+解析
            self.parse(page)


    def parse(self,i):
        driver = webdriver.PhantomJS()
        driver.get(self.url.format(i))

        tree = etree.HTML(driver.page_source)

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
    # for i in range(20):
    #     base_url = 'https://careers.tencent.com/search.html?index={}&keyword=python'.format(i)
    #     Tencent(base_url)
    start = time.time()
    #第一步：创建任务队列并初始化
    #页码，url，请求参数
    base_url = 'https://careers.tencent.com/search.html?index={}&keyword=python'
    queue_page = Queue()
    for i in range(10):
        queue_page.put(i)
    #第二步：创建线程list，这个list的长度就是创建线程的数量，内容就是将来线程名称
    crawl_list = ['aa','bb','cc','dd']
    thread_list = []
    for crawl in crawl_list:
        #创建线程
        #queue_page:将创建好的队列传进去
        #传线程名称
        t = Tencent(base_url,queue_page,crawl)
        t.start()
        thread_list.append(t)
    #阻塞主线程，保证每个都执行完成之后，来测试程序的执行时间
    for t in thread_list:
        t.join()

    print('程序执行的时间：',time.time()-start)
# 程序执行的时间： 24.92959237098694