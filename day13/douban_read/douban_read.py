import json

from selenium import webdriver
from lxml import etree
import re
import requests

def get_content_by_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # 等待
    driver.implicitly_wait(20)
    html_str = driver.page_source
    driver.quit()
    return etree.HTML(html_str)


def get_content_by_request(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    response = requests.get(url,headers=headers)
    return response.text


def parse_detail(item):
    url = item['book_url']
    html_str = get_content_by_request(url)
    html = etree.HTML(html_str)
    try:
        desc = html.xpath('//div[@class="when-expand"]/p/text()|//div[@class="when-fold"]/text()')[0]
        item['desc'] = desc
    except Exception:
        desc = html.xpath('string(//div[@class="info"])')[0]


def parse_ajax(type_name, index):
    '''
    获取每个分类的ajax数据
    :param type_urls:
    :param index:
    :return:
    '''
    ajax_url = 'https://read.douban.com/j/index//charts?type={}&index={}&verbose=1'.format(type_name,index)
    json_str = get_content_by_request(ajax_url)
    json_data = json.loads(json_str)
    if json_data:
        for data in json_data['list']:
            title = data['works']['title']
            book_url = 'https://read.douban.com' + data['works']['url']
            author = data['works']['author'][0]['name']
            abstract = data['works']['abstract']
            wordCount = data['works']['wordCount']
            item = {}
            item['title'] = title
            item['book_url'] = book_url
            item['author'] = author
            item['abstract'] = abstract
            item['wordCount'] = wordCount
            print(item)
            parse_detail(item)


def main():
    base_url = 'https://read.douban.com/charts'
    html = get_content_by_selenium(base_url)
    # 解析分类url
    type_urls = html.xpath('//div[@class="rankings-nav"]/a[position()>1]/@href')
    # print(type_urls)
    # '/charts?type=unfinished_column&index=featured&dcs=charts&dcm=charts-nav
    for url in type_urls:
        p = re.compile(r'type=(.*?)&index=(.*?)&dcs=')
        type_name = p.search(url).group(1)
        index = p.search(url).group(2)
        parse_ajax(type_name,index)


if __name__ == '__main__':
    main()