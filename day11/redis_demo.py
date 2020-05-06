'''
python操作redis
'''

import redis

# 1、创建一个redis连接
re = redis.Redis(host='localhost',port=6379)

# 2、通过连接对象来执行相应的redis命令
# re.set('python','python课程')
# result = re.get('python')
# print(result)
# b'python\xe8\xaf\xbe\xe7\xa8\x8b'
# redis保存的数据都是bytes类型

# 取list的内容
result =re.lrange('l1',0,-1)
# 取hash表
result = re.hget('h1','name')
# 取集合
result = re.sadd('s1','name')