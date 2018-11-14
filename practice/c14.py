'''
字典推导式
'''

students = {
    "a": 1,
    "b": 2,
    "c": 3
}

# 求字典中 key 的值
b = [key for key, value in students.items()]

print(b)

a = [3]
if a:
    print("1")
else:
    print("2")
