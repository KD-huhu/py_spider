import requests
import time
import xlwt
from lxml import etree
from excel_utils.excel_write import ExcelUtils


class MusicWY(object):
    def __init__(self,url):
        self.url = url
        self.main()

    def get_xpath(self,url):
        # 准备参数
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',

        }
        response = requests.get(url,headers = headers)
        time.sleep(1)
        # 测试是否可以获得结果
        # print(response.text)
        html_element = etree.HTML(response.text)
        return html_element

    def get_singer_area(self,url):
        html = self.get_xpath(url)
        area_list = html.xpath('//div[@id="singer-cat-nav"]/div/ul/li/a/@href')
        # 测试是否可以获得结果
        # print(area_list)
        return area_list


    def main(self):
        # 第一步：获取分类歌手列表
        area_singer_list = self.get_singer_area(self.url)
        for area in area_singer_list:
            new_url = 'https://music.163.com' + area
            html = self.get_xpath(new_url)
            # 第二步：获取字母列表
            character_list = html.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')
            # 测试是否可以获得结果
            # print(character_list)
            for character in character_list:
                new_new_url = 'https://music.163.com' + character
                html_character = self.get_xpath(new_new_url)
                # 第三步：在字母列表中获取歌手信息
                li_list = html_character.xpath('//ul[@id="m-artist-box"]/li')
                # print(li_list)
                for li in li_list:
                    try:
                        # 歌手姓名和url
                        singer_name = li.xpath('.//p/a[1]/text()|./a/text()')[0]
                        singer_link = 'https://music.163.com' + li.xpath('.//p/a[1]/@href|./a/@href')[0]
                        item = {}
                        item['歌手名'] = singer_name
                        item['链接'] = singer_link
                        final_list.append(item)
                        print(item)
                    except Exception:
                        pass


if __name__ == '__main__':
    base_url = 'https://music.163.com/discover/artist'
    final_list = []
    MusicWY(base_url)
    ExcelUtils.write_to_excel('MusicWY.xls','singers',final_list)