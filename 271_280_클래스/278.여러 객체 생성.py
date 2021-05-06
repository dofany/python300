# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

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
        self.deposit_count = 0
        self.name = name
        self.code = code
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.code += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                self.code = (self.code * 1.01)


    def withdraw(self, amount):
        if self.code > amount:
            self.code -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ",format(self.code,','))

result = []
a = Account("홍길동",1000000)
b = Account("임꺽정",10000)
c = Account("지드래곤",100000)
result.append(a)
result.append(b)
result.append(c)

for i in result:
    i.display_info()


