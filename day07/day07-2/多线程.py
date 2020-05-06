import threading
import time
import random

def download(filename):
    print(f"{filename}文件开始下载")
    time.sleep(random.random() * 5)
    print(f"{filename}文件下载完成")


if __name__ == '__main__':
    for i in range(5):
        # 创建5个线程，每个线程
        t = threading.Thread(target=download, args=(i,))
        t.start()

'''
0文件开始下载
1文件开始下载
2文件开始下载
3文件开始下载
4文件开始下载
3文件下载完成
1文件下载完成
2文件下载完成
0文件下载完成
4文件下载完成
'''