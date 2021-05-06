# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
#
# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 100

class Car:
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price

class Bicycle(Car):
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price

bicycle = Bicycle(2,100)
print(bicycle.price)
