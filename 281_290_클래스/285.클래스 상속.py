# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
#
# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000

class Car:
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price

class Car2(Car):
    def __init__(self,tire,price):
        super().__init__(tire,price)

    def inter(self):
        print("바퀴수 ", self.tire)
        print("가격 ", self.price)

car = Car2(4,1000)
car.inter()