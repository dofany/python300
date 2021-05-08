# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
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

    def inter(self):
        super().inter()
        print("구동계 ", self.ride)


bicycle = Bicycle(2, 100, "시마노")
bicycle.inter()

