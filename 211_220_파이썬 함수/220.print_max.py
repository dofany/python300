# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

def print_max(x,y,z):
    if x > y:
        if y > z:
            print(x)
    if x < y:
        if y > z:
            print(y)
    if x < y:
        if y < z:
            print(z)

print_max(3,4,5)
