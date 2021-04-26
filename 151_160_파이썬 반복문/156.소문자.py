# 리스트에서 소문자만 화면에 출력하라.
#
# 리스트 = ["A", "b", "c", "D"]
# b
# c

lst = ["A","b","c","D"]
for i in lst:
    if i.islower()==True:
        print(i)