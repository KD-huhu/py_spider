import threading
import time
import random

def sing():
    for i in range(3):
        print("正在唱歌---{}".format(i))
        time.sleep(random.random())

def dance():
    for i in range(3):
        print("正在跳舞---{}".format(i))
        time.sleep(random.random())

# 主线程代码
if __name__ == '__main__':
    # 打印晚会开始时间
    print("晚会开始: {}".format(time.ctime()))
    # 分别创建执行sing和dance函数的线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 主线程
    t1.start()
    t2.start()
    # 阻止主线程终止
    while True:
        # 查看线程数量（包括主线程，至少含有一个主线程）
        length = len(threading.enumerate())
        # 主线程加上两个子线程的线程，一共三个线程
        print('当前运行的线程数为: {}'.format(length))
        time.sleep(1)
        if length <= 1:
            break

'''
晚会开始: Mon Apr 27 21:41:08 2020
正在唱歌---0
正在跳舞---0
当前运行的线程数为: 3
正在唱歌---1
正在跳舞---1
正在唱歌---2
当前运行的线程数为: 3
正在跳舞---2
当前运行的线程数为: 2
当前运行的线程数为: 1
'''