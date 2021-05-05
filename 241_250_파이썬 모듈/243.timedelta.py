# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

import datetime

today = datetime.datetime.today()
for i in range(5,0,-1):
    day = datetime.timedelta(days=i)
    print(today-day)