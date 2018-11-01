def factory(pos):
    def go(step):
        nonlocal pos
        result = pos +step
        pos = result
        return result
    return go

f = factory(0)
print(f(2))
print(f(3))
print(f(6))