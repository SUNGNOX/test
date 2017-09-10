# -*- coding:utf-8 -*-
import threading
import time

#用Condion实现生产消费模型
#Condion默认与Rlock关联，一个线程拥有一个锁
cn = threading.Condition()
productor = None

def product():
    global productor
    if cn.acquire():
        while True:
            if productor is None:
                print('Beging product something...')
                productor ='things'
                cn.notify()
            cn.wait()
            time.sleep(2)

def consume():
    global productor
    if cn.acquire():
        while True:
            if productor is not None:
                print('Beging consume...')
                productor = None
                cn.notify()
            cn.wait()
            time.sleep(2)

prdct = threading.Thread(target=product)
cmsm = threading.Thread(target=consume)

cmsm.start()
prdct.start()
# prdct.join()
# cmsm.join()
