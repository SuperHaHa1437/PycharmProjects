def curve_pre():
    a = 25

    def curve():
        # nonlocal a
        result = a ** 2
        # a = result
        return result

    return curve


f = curve_pre()
print(f.__closure__)
print(f())
