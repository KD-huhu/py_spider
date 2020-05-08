import requests

class Spider(object):

    def __init__(self):
        self.url = "http://www.biquyun.com/14_14055/"
        self.base_url = "http://www.biquyun.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/62.0.835.163 Safari/535.1"
        }
        self.title = ""

    def get_pager_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                return response.text.encode("iso-8859-1")
        except Exception:
            print("请求异常")
            return None

if __name__ == '__main__':
    s = Spider()


'''
https://www.52bqg.com/book_84329/25257582.html
https://www.52bqg.com/book_84329/25257583.html
https://www.52bqg.com/book_84329/25257584.html

https://www.52bqg.com/book_84329/25257654.html

https://www.52bqg.com/book_84329/32348447.html
https://www.52bqg.com/book_84329/32348465.html
'''