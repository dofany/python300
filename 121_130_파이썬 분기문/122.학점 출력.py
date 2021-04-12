# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
#
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A

score = int(input("score: "))

if 100 >= score >= 81:
    print("grade is A")
elif 80 >= score >= 61:
    print("grade is B")
elif 60 >= score >= 41:
    print("grade is C")
elif 40 >= score >= 21:
    print("grade is D")
else:
    print("E")