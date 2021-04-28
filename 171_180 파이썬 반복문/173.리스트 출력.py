#
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500


price_list = [32100, 32150, 32000, 32500]
result = len(price_list)
for i in price_list:
    result -= 1
    print(result,i)