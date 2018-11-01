'''
装饰器
装饰器与特定的函数绑定没有意义
适配不同的函数才是装饰器的意义
'''
import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


# 单参数
@decorator
def f1(funcname):
    print('this is a function' + funcname)


# 多参数
@decorator
def f2(funcname1, funcname2):
    print('this is a function' + funcname1)
    print('this is a function' + funcname2)


# 关键字参数
@decorator
def f3(funcname1, funcname2, **kw):
    print('this is a function' + funcname1)
    print('this is a function' + funcname2)
    print(kw)


f1("test func")
f2("test func1", "test func2")
f3("test func1", "test func2", a=1, b=2, c="123")

# f = decorator(f1)
# f()
