# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100

class Car:
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price

    def inter(self):
        print("바퀴수 :",self.tire)
        print("가격 :",self.price)

class Car2(Car):
    def __init__(self,tire,price):
        super().__init__(tire,price)

class Bicycle(Car):
    def __init__(self,tire,price,ride):
        super().__init__(tire,price)
        self.ride = ride


bicycle = Bicycle(2, 100, "시마노")
bicycle.inter()
