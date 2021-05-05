# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.
#
# 종목명	종목코드	PER	PBR	배당수익률
# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37

class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

result = []
samsung = Stock("삼성전자","005930",15.79,1.33,2.83)
hyundae = Stock("현대차","005380",8.70,0.35,4.27)
lg = Stock("LG전자","066570",317.34,0.69,1.37)

result.append(samsung)
result.append(hyundae)
result.append(lg)

for i in result:
    print("종목명: {} 종목코드: {} PER: {} PBR: {} 배당수익률:{} ".format(i.name, i.code, i.per, i.pbr, i.dividend))


