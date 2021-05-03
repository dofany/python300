# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
#
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

def print_5xn(line):
    str = int(len(line)/5)

    for i in range(str+1):
        print(line[i*5: i*5+5])

print_5xn("아이엠어보이유알어걸")
