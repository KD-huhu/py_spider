import requests
import time
import xlwt
from lxml import etree
from excel_utils.excel_write import ExcelUtils


def get_xpath(url):
    '''
    请求url，获取页面内容的element对象
    :param url: 对应url
    :return: 对应页面的element对象
    '''
    # 准备参数
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',

    }
    # 请求url，获取响应
    response = requests.get(url,headers = headers)
    time.sleep(1)
    # 将页面内容变成element
    html = etree.HTML(response.text)
    # 测试是否可以获得数据
    # print(html)
    # <Element html at 0x18661ded788>
    return html


def page_parse(html):
    '''
    解析页面，提取数据
    :param html: 对应页面的element对象
    :return: 提取到的数据
    '''
    # 取出所有tr标签
    tr_list = html.xpath('//tr')
    # 测试是否可以提取数据
    # print(tr_list)
    for tr in tr_list:
        try:
            english = tr.xpath('.//strong/text()')[0]
            chinese = tr.xpath('.//td[@class="span10"]/text()')[0].strip()
            # 测试是否可以提取翻译
            # print(english)
            item = {}
            item['英文'] = english
            item['中文'] = chinese
            # print(item)
            word_list.append(item)
        except Exception:
            pass


def main():
    base_url = 'https://www.shanbay.com/wordlist/110521/232414/?page=%s'
    for i in range(1,4):
        html = get_xpath(base_url %(i))
        page_parse(html)
    ExcelUtils.write_to_excel('word.xls','python单词',word_list)


if __name__ == '__main__':
    word_list = []
    main()
    # print(word_list)