from selenium import webdriver
from lxml import etree
import threading
import time

def parse_page(i):
    drive = webdriver.PhantomJS()
    drive.get(f'https://careers.tencent.com/search.html?index={i}&keyword=python')
    tree = etree.HTML(drive.page_source)
    div_list = tree.xpath('//div[@class="recruit-list"]')

    for div in div_list:
        # 提取
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
        print(item)


if __name__ == '__main__':
    start_time = time.time()
    # 定义一个用来存储线程的list
    crawl_list = []
    for i in range(10):
        '''
        开启线程方法，在爬虫里面有很大弊端，很难控制线程数量。
        设计使用线程来爬去的时候，一个线程爬取一页
        '''
        # 创建一个线程
        t = threading.Thread(target=parse_page,args=(i,))
        t.start()
        crawl_list.append(t)

    for t in crawl_list:
        t.join()
        # join方法的作用就是阻塞当前线程，知道调用他的这个t执行完毕为止。
        # 阻塞主线程，直到所有的子线程全部被调用后再进行主线程
    print('程序运行时间：', time.time() - start_time)
    # 程序运行时间： 8.266629219055176