import time
import random

'''
单线程程序：按照程序的流程取按行执行。
在python中一切皆对象。
'''

# 单线程


def download(filename):
    print(f"{filename}文件开始下载")
    time.sleep(random.random() * 5)
    print(f"{filename}文件下载完成")


if __name__ == '__main__':
    for i in range(5):
        download(i)

'''
0文件开始下载
0文件下载完成
1文件开始下载
1文件下载完成
2文件开始下载
2文件下载完成
3文件开始下载
3文件下载完成
4文件开始下载
4文件下载完成
'''