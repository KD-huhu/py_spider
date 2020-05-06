from selenium import webdriver
from lxml import etree
import threading
import time

def main():
    drive = webdriver.PhantomJS()
    for i in range(10):
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
    main()
    print('程序运行时间：', time.time() - start_time)
    # 程序运行时间： 11.157322406768799