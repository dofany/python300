# for문을 사용해서 3의 배수만을 출력하라.
#
# 리스트 = [3, 100, 23, 44]
# 3

lst = [3, 100, 23, 44]
for i in lst:
    if i % 3 == 0:
        print(i)