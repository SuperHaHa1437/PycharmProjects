list_x = [1, 2, 3, 4]


def square_sum(value):
    def square(x):
        result = x ** value
        return result

    return square


f = square_sum(2)
# print(f.__closure__[0].cell_contents)
for i in list_x:
    print(f(i))

