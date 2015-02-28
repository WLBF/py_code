#coding:utf-8
from urllib2 import *
from re import *
import os
import socket
import time
import threading
 
mylock = threading.RLock()
 
num = 99400000
upbound =99500000
timeout = 60
 
socket.setdefaulttimeout(timeout)
 
path=r"c:/student_image/"
new_path = os.path.join("c:/","student_image")
if not os.path.isdir(new_path):
    os.makedirs(new_path)
 
 
class get_img(threading.Thread):
    def __init__(self, num ):
        threading.Thread.__init__(self)
        self.thread_stop = True
    
 
 
    def run(self):
        global num
        while num <= upbound:
            mylock.acquire()
            print num
            imgurl = r"http://XXXXXXXXXXXXXX/xszp/"+str(num)+r".jpg"
            try:
                filename = imgurl.split("/")[-1]
                f = urlopen(imgurl)
                data = f.read()
                with open(path+filename, "wb") as jpg:
                    jpg.write(data)
                f.close()
            except HTTPError:
                pass
            except URLError:
                pass
            num+=1
            mylock.release()
 
    def stop(self):
        self.thread_stop = True
 
thread_pool=[]
 
def start_download():
    for i in range(0,100):
        thread_pool.append(get_img(num))
    for thread in thread_pool:
        thread.start()
 
if __name__=='__main__':
    start_download()
