# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500

result = -1
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
    result += 1
    print(result,i)