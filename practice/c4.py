def f1():
    # a 为环境变量
    a = 10

    def f2():
        # f2为定义函数，a 必须要在定义函数内被引用,闭包与f2定义函数内部是否有返回结果无关
        nonlocal a
        a += 1
        return a

    return f2


f = f1()
print(f())
print(f.__closure__)
