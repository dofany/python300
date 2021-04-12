# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
#
# >> a
# A
# 힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.

a = input()
if a > chr(90) and a <= chr(122):
    print(a.upper())
else:
    print(a.lower())

#97 <= 122 : a~z

#65 <= 90 : A~Z