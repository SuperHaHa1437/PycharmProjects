class Test():
    def __bool__(self):
        print("boo;")
        return False

    def __len__(self):
        print("len")
        return True


print(len(Test()))
print(bool(Test()))
