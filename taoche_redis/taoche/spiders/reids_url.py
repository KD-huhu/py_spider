import redis
'''
主机才有这个代码，表示初始化任务list
'''
from taoche.spiders.city import CAR_CODE_LIST,CITY_CODE

re_client = redis.Redis()
for city in CITY_CODE:
        for car in CAR_CODE_LIST:
            base_url = 'https://{}.taoche.com/{}/?page=1'.format(city, car)
            print(base_url)
            re_client.rpush('taoche:start_urls',base_url)