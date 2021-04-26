# 이름의 첫 글자를 대문자로 변경해서 출력하라.
#
# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
# (참고) upper() 메서드는 문자열을 대문자로 변경합니다.
#
# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC

lst = ['dog','cat','parrot']
for i in lst:
    print(i[0].upper()+i[1:])