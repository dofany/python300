# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
#
# 삼성 = Stock("삼성전자", "005930")

class Stock:
    def __init__(self,menu,code):
        self.menu = menu
        self.code = code

    def set_menu(self,menu):
        self.menu = menu

    def set_code(self,code):
        self.code = code

    def get_menu(self):
        return self.menu

    def get_code(self):
        return self.code


samsung = Stock("삼성전자","005930")
print(samsung.menu)
print(samsung.code)
print(samsung.get_menu())
print(samsung.get_code())
