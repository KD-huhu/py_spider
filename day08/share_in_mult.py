# 多线程--全局变量--共享
from threading import Thread
import time
import random

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1
        time.sleep(random.random())
        print('in work1, g_num = %d' %g_num)


def work2():
    global g_num
    for i in range(3):
        g_num += 1
        time.sleep(random.random())
        print('in work2, g_num = %d' %g_num)


if __name__ == '__main__':
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)
    t1.start()
    t2.start()

'''
in work1, g_num = 102
in work2, g_num = 103
in work1, g_num = 104
in work2, g_num = 105
in work2, g_num = 106
in work1, g_num = 106
'''