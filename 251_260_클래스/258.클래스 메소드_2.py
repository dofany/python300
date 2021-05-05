# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
#
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름:", self.name, ", 나이:", self.age, ", 성별:", self.sex)

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("모름",0,"모름")
areum.who()

areum.setInfo("아름",25,"여자")
areum.who()

