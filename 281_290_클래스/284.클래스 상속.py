# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노

class Car:
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price

class Bicycle(Car):
    def __init__(self,tire,price,ride):
        super().__init__(tire,price)
        self.ride = ride

bicycle = Bicycle(2,100,"시마노")
print(bicycle.ride)
