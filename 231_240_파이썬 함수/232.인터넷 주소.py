# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
#
# make_url("naver")
# www.naver.com

def make_url(a):
    url = "www."+a+".com"
    return url

print(make_url("naver"))

