# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
#
# a = Stock(None, None)
# a.set_name("삼성전자")

class Stock:
    def __init__(self,menu,code):
        self.menu = menu
        self.code = code

    def set_menu(self,menu):
        self.menu = menu

a = Stock(None,None)
a.set_menu("삼성전자")
print(a.menu)


