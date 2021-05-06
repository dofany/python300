# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

import random

class Account:
    count = 0

    def __init__(self,name,code):
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

a = Account("홍길동",100)
print(Account.count)
a = Account("임꺽정",100)
print(Account.count)



