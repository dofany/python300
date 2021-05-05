# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
#
# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름:", self.name, ", 나이:", self.age, ", 성별:", self.sex)

    def __del__(self):
        print("나의 죽음을 알리지 마라")

areum = Human("아름",25,"여자")
del(areum)