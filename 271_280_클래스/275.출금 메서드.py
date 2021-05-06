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

    def withdrwa(self,amount):
        if self.code > amount:
            self.code -= amount

a = Account("홍길동",100)
a.deposit(100)
a.withdrwa(90)
print(a.code)