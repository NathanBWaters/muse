from multiprocessing import Process
import os
import time

def info(title):
    while True:
        print title
        time.sleep(3)

if __name__ == '__main__':
    p = Process(target=info, args=('bob',))
    n = Process(target=info, args=('kathy',))
    p.start()
    n.start()
