c = 50


def add(a, b):
    global c
    c = a + b
    print(id(c))
    print(c)

add(1,2)
print(id(c))
print(c)
