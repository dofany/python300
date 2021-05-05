# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.
#
# a = Stock(None, None)
# a.set_code("005930")

class Stock:
    def __init__(self,menu,code):
        self.menu = menu
        self.code = code

    def set_code(self,code):
        self.code = code

a = Stock(None,None)
a.set_code("005930")
print(a.code)