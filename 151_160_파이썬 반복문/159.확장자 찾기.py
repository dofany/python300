# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
#
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h

lst = ['intra.h','intra.c','define.h','run.py']
for i in lst:
    result = i.split('.')
    if result[1] == 'h':
        print(i)