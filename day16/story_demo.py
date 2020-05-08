import random
import smtplib
from email.mime.text import MIMEText
import requests
from lxml import etree


class Sleep_story(object):
    def __init__(self,url):
        self.url = self.init_url(base_url)
        self.parse()

    def init_url(self,url):
        # 确定要爬取哪一页
        # 先生成随机数来表示获取那一页
        page = random.randint(0,71)
        if page==0:
            return url.format('')
        else:
            return url.format('_' + str(page))

    def get_xpath(self,url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        response = requests.get(url,headers=headers)
        return etree.HTML(response.content.decode('utf-8'))

    def send_email(self,text):
        # 定义发件人
        msg_from = '@qq.com'
        # 授权码
        password = ''
        # 发件人
        msg_to = '@qq.com'
        subject = text[0]
        # print(subject)
        # 邮件对象
        #
        msg = MIMEText(text[1], 'plain', 'utf-8')
        msg['From'] = msg_from
        msg['To'] = msg_to
        msg['Subject'] = subject
        try:
            # 创建stmp对象
            smtp = smtplib.SMTP()
            # 链接哪个服务器
            smtp.connect('smtp.qq.com')
            # 登录
            smtp.login(msg_from, password)
            # 发送
            smtp.sendmail(msg_from, msg['To'].split(';'), msg.as_string())
            print('发送成功！')

        except Exception:
            print('邮件发送失败！')

    def parse_story(self,url):
        html = self.get_xpath(url)
        story_name = html.xpath('//h1/text()')[0]
        story_content = html.xpath('string(//div[@class="t_news_txt"])')
        self.send_email((story_name,story_content))

    def parse(self):
        html = self.get_xpath(self.url)
        # 先获取改页的所有dd
        dd_list = html.xpath('//dl[@class="txt_box"]/dd')
        # print(dd_list)
        # 从中随机取出一个
        dd_choice = random.choice(dd_list)
        # 获取详情页链接
        story_url = dd_choice.xpath('.//a/@href')[0]
        # print(story_url)
        self.parse_story('http://www.tom61.com' + story_url)


if __name__ == '__main__':
    base_url = 'http://www.tom61.com/ertongwenxue/shuiqiangushi/index{}.html'
    Sleep_story(base_url)