import re

'''
公司：所有员工工资都是记录在一个txt
    zhangsan:2000,lisi:3000
'''

#函数任务是对传入的字符串中的工资加1000
def func(m):
    return str(int(m.group(1))+1000)

def func1(m):
    return 'zhangsan' + str(int(m.group(1)) + 1000)

content = 'zhangsan:2000,lisi:3000'

#1、张三工资涨1000
p2 =re.compile(r'zhangsan:(\d+)')
print(p2.sub(func1,content))

#2、每个人涨1000
# p3 =re.compile(r'(\d+)')
# print(p3.sub(func,content))
#zhangsan:3000,lisi:4000