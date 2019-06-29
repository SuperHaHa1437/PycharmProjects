"""
Created by 张 on 2019/6/4 
"""
__author__ = '张'
from werkzeug.local import Local
import threading, time


class A():
    b = 1


obj = Local()
obj.b = 1
print("obj is " + str(obj.b))


def work():
    obj.b = 2
    print('in new thread b is ' + str(obj.b))


new_t = threading.Thread(target=work, name='zhang')
new_t.start()
time.sleep(1)

print('in main thread b is ' + str(obj.b))
