# 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요

class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_per(self,per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

a = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
a.set_per(12.75)
print(a.per)