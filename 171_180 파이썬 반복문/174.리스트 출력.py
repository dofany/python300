# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500

price_list = [32100, 32150, 32000, 32500]
result = price_list[1:]
num = 90

for i in result:
    num += 10
    print(num,i)
