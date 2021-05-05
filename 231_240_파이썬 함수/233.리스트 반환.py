# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
#
# make_list("abcd")
# ['a', 'b', 'c', 'd']

def make_list(s):
    array = []
    for i in s:
        array.append(i)
    return array
print(make_list("abcd"))
