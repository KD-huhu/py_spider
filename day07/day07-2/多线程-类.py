import threading
import time
import random

class Mythread(threading.Thread):
    def __init__(self,filename):
        # 调用父类的init方法
        super().__init__()
        self.filename = filename
    # def __init__(self,filename,name):
    #     # 调用父类的init方法
    #     super().__init__()
    #     self.filename = filename
    #     # 使用name属性来为不同进程取名
    #     self.name = name

    # run方法就是线程启动后执行的方法
    # start--->run
    def run(self):
        self.download(self.filename)

    def download(self,filename):
        print(f"{filename}文件开始下载 @{self.name}")
        time.sleep(random.random() * 5)
        print(f"{filename}文件下载完成 @{self.name}")


if __name__ == '__main__':
    name_list = ['a','b','c','d','e']
    for i in range(5):
        t = Mythread(i,)
        t.start()

'''
默认进程名称：
0文件开始下载 @Thread-1
1文件开始下载 @Thread-2
2文件开始下载 @Thread-3
3文件开始下载 @Thread-4
4文件开始下载 @Thread-5
0文件下载完成 @Thread-1
2文件下载完成 @Thread-3
3文件下载完成 @Thread-4
4文件下载完成 @Thread-5
1文件下载完成 @Thread-2
'''

'''
更改进程名称后：
    0文件开始下载 @a
    1文件开始下载 @b
    2文件开始下载 @c
    3文件开始下载 @d
    4文件开始下载 @e
    0文件下载完成 @a
    2文件下载完成 @c
    1文件下载完成 @b
    3文件下载完成 @d
    4文件下载完成 @e
'''