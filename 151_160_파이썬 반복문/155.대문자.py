# 리스트에서 대문자만 화면에 출력하라.
#
# 리스트 = ["A", "b", "c", "D"]
# A
# D
# (참고) isupper() 메서드는 대문자 여부를 판별합니다.
#
# >> 변수 = "A"
# >> 변수.isupper()
# True
# >> 변수 = "a"
# >> 변수.isupper()
# False

lst = ["A","b","c","D"]
for i in lst:
    if i.isupper()==True:
        print(i)
