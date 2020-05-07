# 去重操作
import hashlib
import redis
from scrapy.exceptions import IgnoreRequest


class MyMiddler(object):
    def __init__(self):
        pass

    def get_md5(self, value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()

    def url_seen(self, url):
        '''
        判断url是否重复
        :param url:
        :return:True：重复，False不重复
        '''
        re = redis.Redis()
        result = re.sadd('maoyan_actor_set', url)
        return result == 0

    def process_request(self, request, spider):
        # print('in middler')
        if not self.url_seen(self.get_md5(request.url)):
            return None  # 继续下载处理
        else:
            # print('33333')
            raise IgnoreRequest