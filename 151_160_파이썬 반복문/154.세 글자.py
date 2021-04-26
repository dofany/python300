# 리스트에서 세 글자 이상의 문자를 화면에 출력하라
#
# 리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language

lst = ["I","study","python","language","!"]
for i in lst:
    if len(i) >= 3:
        print(i)