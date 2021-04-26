# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
#
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h

lst = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in lst:
    result = i.split('.')
    if result[1] == 'h' or result[1]=='c':
        print(i)