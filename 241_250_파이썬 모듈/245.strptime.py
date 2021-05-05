# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
#

import datetime
today = "2020-05-04"
data = datetime.datetime.strptime(today,"%Y-%m-%d")
print(data)