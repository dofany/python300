# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.
#
# 항목	정보
# 종목명	삼성전자
# 종목코드	005930
# PER	15.79
# PBR	1.33
# 배당수익률	2.83

class Stock:
    def __init__(self,menu,code,per,pbr,price):
        self.menu = menu
        self.code = code
        self.per = per
        self.pbr = pbr
        self.price = price

a = Stock("삼성전자","005930",float(15.79),float(1.33),float(2.83))
print(a.menu)
print(a.code)
print(a.per)
print(a.pbr)
print(a.price)
