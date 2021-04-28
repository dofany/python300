# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
#
# 합: 25

result = 0
for i in range(1,10):
    if i % 2 != 0:
        result += i
print(result)