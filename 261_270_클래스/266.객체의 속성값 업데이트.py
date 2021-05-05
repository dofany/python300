# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.

class Stock:
    def __init__(self,menu,code,per,pbr,price):
        self.menu = menu
        self.code = code
        self.per = per
        self.pbr = pbr
        self.price = price



