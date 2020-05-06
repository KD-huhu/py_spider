import re
import json
from typing import TextIO

import requests
import time

def get_content(url):
    '''
    请求给定url的页面，返回页面内容
    :param url:
    :return:
    '''
    # headers参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    }
    # 发送请求，获取响应
    respose = requests.get(url,headers = headers)
    time.sleep(1)
    if respose.status_code == 200:
        return respose.text
    else:
        return ''


def parse_html(html_str):
    '''
    从页面的str中使用正则提取信息
    :param html_str:
    :return:
    '''
    #print(html_str)
    # 电影名称、演员、上映时间、评分、详情页链接

    # 定位到电影列表标签
    dl_p = re.compile(r'<dl class="board-wrapper">.*?</dl>',re.S)
    # 注意一定要在末尾加上： re.S 表示匹配空白字符
    dl_content = dl_p.search(html_str).group()
    # 注意对于匹配得到的使用 group 获得内容
    # print(dl_content)
    dd_p = re.compile(r'<dd>.*?</dd>',re.S)
    dd_list = dd_p.findall(dl_content)
    # print(len(dd_list))
    for dd in dd_list:
        #电影名称
        move_name_p = re.compile(r'title="(.*?)" class="image-link"',re.S)
        move_name = move_name_p.search(dd).group(1)
        #print(move_name)
        # 注意提取 group 内容
        # 演员
        actor_p = re.compile(r'<p class="star">(.*?)</p>',re.S)
        actor = actor_p.search(dd).group(1).strip()
        # .strip 函数是去除空白字符
        # print(actor)
        # 上映时间
        data_p = re.compile(r'<p class="releasetime">(.*?)</p>',re.S)
        data = data_p.search(dd).group(1)
        # print(data)
        # 评分
        score_p = re.compile(r'<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>',re.S)
        score = score_p.search(dd).group(1) + score_p.search(dd).group(2)
        # print(score)
        # 详情页链接
        link_p = re.compile(r'<a href="(.*?)" title=',re.S)
        link = 'https://maoyan.com' + link_p.search(dd).group(1)
        # print(link)
        item = {}
        item['move_name'] = move_name
        item['actor'] = actor
        item['data'] = data
        item['score'] = score
        item['link'] = link
        #print(item)
        move_list.append(item)


def write_to_json(move_list):
    '''
    将电影爬取内容列表写入 json 文件
    :param move_list:
    :return:
    '''
    # json.dump(list/dict,fp)---将list或者dict写入json文件
    with open('movie.json', 'w', encoding='utf-8') as fp:
        json.dump(move_list,fp)
    with open('movie.txt', 'w', encoding='utf-8') as fp1:
        for i,item in enumerate(move_list,1):
            fp1.write(str(i) + ':' + str(item) + '\n')
    # for i, item in enumerate(move_list, 1):
    #     print(i,item,sep=':')
    print("写入文件成功！")


def main():
    # 确定基础url
    base_url = 'https://maoyan.com/board/4?offset=%s'
    # 获取每一页的内容
    for i in range(10):
        html_str = get_content(base_url %(i * 10))
        # 提取每一页内容信息
        parse_html(html_str)
    # 得到每一页的中电影的内容后，将move_list 列表写入 json 文件
    write_to_json(move_list)


if __name__ == '__main__':
    move_list = []
    main()
