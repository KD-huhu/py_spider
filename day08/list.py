# 列表（容器）当做实参传递到线程中
import threading
import time
import copy

'''
当列表作为线程任务函数参数,如果对列表做一些更改，需要拷贝一份作为遍历的内容
'''

def work1(download_list, finish_list):
    # copy_list = copy.copy(download_list)
    # for file in copy_list:
    #     print("----in work1---download:%d" %file)
    #     time.sleep(1)
    #     # 下载完成之后
    #     # 1、任务列表中移除已经下载的元素
    #     download_list.remove(file)
    #     finish_list.append(file)
    '''
    [11, 22, 33] []
    当前下载进度：0.00% [<_MainThread(MainThread, started 14824)>, <Thread(Thread-1, started 12976)>]
    [11, 22, 33] []
    当前下载进度：0.00% [<_MainThread(MainThread, started 14824)>, <Thread(Thread-1, started 12976)>]
    ----in work1---download:22
    [22, 33] [11]
    当前下载进度：33.33% [<_MainThread(MainThread, started 14824)>, <Thread(Thread-1, started 12976)>]
    ----in work1---download:33
    [33] [11, 22]
    当前下载进度：66.67% [<_MainThread(MainThread, started 14824)>, <Thread(Thread-1, started 12976)>]
    [] [11, 22, 33]
    当前下载进度：100.00% [<_MainThread(MainThread, started 14824)>]
    全部下载完成！
    '''
    #copy_list = copy.copy(download_list)
    for file in download_list:
        print("----in work1---download:%d" % file)
        time.sleep(1)
        # 下载完成之后
        # 1、任务列表中移除已经下载的元素
        download_list.remove(file)
        finish_list.append(file)
    '''
    [11, 22, 33] []
    当前下载进度：0.00% [<_MainThread(MainThread, started 3876)>, <Thread(Thread-1, started 200)>]
    [11, 22, 33] []
    当前下载进度：0.00% [<_MainThread(MainThread, started 3876)>, <Thread(Thread-1, started 200)>]
    ----in work1---download:33
    [22] [11, 33]
    当前下载进度：66.67% [<_MainThread(MainThread, started 3876)>]
    [22] [11, 33]
    当前下载进度：66.67% [<_MainThread(MainThread, started 3876)>]
    [22] [11, 33]
    当前下载进度：66.67% [<_MainThread(MainThread, started 3876)>]
    [22] [11, 33]
    当前下载进度：66.67% [<_MainThread(MainThread, started 3876)>]
    '''


if __name__ == '__main__':
    # 下载任务列表
    download_list = [11, 22, 33]
    # 总任务列数
    total = len(download_list)
    # 下载完成列表
    finish_list = []
    t1 = threading.Thread(target=work1, args=(download_list, finish_list))
    t1.start()
    while True:
        print(download_list, finish_list)
        pro = len(finish_list) / total
        print("当前下载进度：%.2f%%" %(pro*100),threading.enumerate())
        time.sleep(1)
        if pro == 1:
            print("全部下载完成！")
            break
