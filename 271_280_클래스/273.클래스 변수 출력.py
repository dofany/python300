# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

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

a = Account("홍길동",100)
b = Account("임꺽정",100)
a.get_account_num()