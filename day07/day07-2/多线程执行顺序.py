import threading
import time
import random

class Mythread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I`m " + self.name + "@" + str(i)
            print(msg)
            time.sleep(1)

if __name__ == '__main__':
    for i in range(2):
        t = Mythread()
        t.start()

'''
I`m Thread-2@0
I`m Thread-1@0
I`m Thread-1@1
I`m Thread-2@1
I`m Thread-1@2
I`m Thread-2@2
'''