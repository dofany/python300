# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
#
# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자

class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름:",self.name,", 나이:",self.age,", 성별:",self.sex)

human = Human("조아름",25,"여자")
human.who()
