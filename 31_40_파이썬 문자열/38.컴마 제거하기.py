# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"

samsung = "5,969,782,550"
result = samsung.replace(',',"")
result = int(result)
print(result, type(result))
