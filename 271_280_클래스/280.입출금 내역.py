# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

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
        self.deposit_log = []
        self.withdraw_log = []
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
            self.deposit_log.append(amount)
            self.code += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                self.code = (self.code * 1.01)


    def withdraw(self, amount):
        if self.code > amount:
            self.withdraw_log.append(amount)
            self.code -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ",format(self.code,','))

    def deposit_history(self):
        for i in self.deposit_log:
            print("{}원이 입금되었습니다.".format(i))

    def withdraw_history(self):
        for i in self.withdraw_log:
            print("{}원이 출금되었습니다.".format(i))



a = Account("홍길동",1000000)
a.deposit(100)
a.deposit_history()

