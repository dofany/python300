# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
#
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

def print_mxn(line,x):
    str = int(len(line) / x)

    for i in range(str + 1):
        print(line[i * x: i * x + x])


print_mxn("아이엠어보이유알어걸",3)