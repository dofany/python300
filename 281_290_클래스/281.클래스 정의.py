# 다음 코드가 동작하도록 차 클래스를 정의하세요.
#
# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000

class Car:
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price


car = Car(2,1000)
print(car.tire)
print(car.price)