# 차 클래스를 상속받은 자전차 클래스를 정의하세요.

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
