# def print_student(name, gender="male", age=18, collage="beijing"):
#     print("i am " + name)
#     print("i am " + gender)
#     print("i am " + str(age))
#     print("i am " + collage)
#
#
# print_student("zhang","famale",collage="cs",age=12)

class Student():
    name = "a"
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        # print(self.__class__.name)
        # print(self.__class__.age)

    def do_homework(self):
        print("homework")

    def marking(self, score):
        if score < 0:
            print("error")
        else:
            self.__score = score
            print("score:" + str(score))


student = Student("zhang", 12)
# print(student.name, student.age)
student.marking(99)
print(student._Student__score)