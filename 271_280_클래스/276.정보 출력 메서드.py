# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
#
# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원

# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

import random

class Account:
    count = 0

    def __init__(self, name, code):
        self.name = name
        self.code = code

        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.count += 1

    @classmethod
    def get_account_num(cnt):
        print(cnt.count)

    def deposit(self,amount):
        if amount >= 1:
            self.code += amount

    def withdraw(self,amount):
        if self.code > amount:
            self.code -= amount

    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account_number))
        print("잔고: ",format(self.code,','))

a = Account("홍길동",1000000000)
a.display_info()