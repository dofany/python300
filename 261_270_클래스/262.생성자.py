# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
#
# 삼성 = Stock("삼성전자", "005930")

class Stock:
    def __init__(self,menu,code):
        self.menu = menu
        self.code = code

ju = Stock("삼성전자","005930")
print(ju.menu)
print(ju.code)