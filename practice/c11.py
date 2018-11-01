list_x = [0, 1, 0, 1, 1, 0]
list_u = ['a', 'A', 'b', 'N']
# r = filter(lambda x: True if x == 1 else False, list_x)
# r = filter(lambda x: x, list_x)  # lambda 表达式的 x 也可以代表返回的结果真假
r = filter(lambda x: x.islower(), list_u)  # lambda 表达式的 x 也可以代表返回的结果真假
print(list(r))
