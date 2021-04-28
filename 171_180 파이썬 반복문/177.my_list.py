# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
#
# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가

my_list = ["가", "나", "다", "라"]
for i in range(1,len(my_list)):
    print(my_list[4-i],my_list[3-i])
