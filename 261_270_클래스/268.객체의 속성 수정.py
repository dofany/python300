# PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

class Stock:
    def __init__(self,menu,code,per,pbr,dividend):
        self.menu = menu
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


