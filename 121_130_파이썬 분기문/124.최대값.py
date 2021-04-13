# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
#
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20

number1 = int(input("input number1: "))
number2 = int(input("input number2: "))
number3 = int(input("input number3: "))

data = [number1,number2,number3]
print(max(data))

