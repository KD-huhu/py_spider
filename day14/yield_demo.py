def gen_num(num):
    '''
    定义这个函数成为生成器
    :param num:
    :return:
    '''
    for i in range(num):
        yield i

for i in gen_num(10):
    print(i)

'''
0
1
2
3
4
5
6
7
8
9
'''