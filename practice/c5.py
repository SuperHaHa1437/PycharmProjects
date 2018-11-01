'''闭包方式'''
origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        result = pos + step
        pos = result
        return result

    return go


f = factory(origin)
print(f(2))
print(f(3))
print(f(6))
'''非闭包方式'''
# origin = 0
#
#
# def go(step):
#     global origin
#     new_pos = origin + step
#     origin = new_pos
#     return new_pos


# print(go(2))
# print(go(3))
# print(go(6))
