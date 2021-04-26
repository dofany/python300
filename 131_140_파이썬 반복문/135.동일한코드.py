# for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
#
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)

arr = ["A","B","C"]
print("변환: {0}".format(arr[0].lower()))
print("변환: {0}".format(arr[1].lower()))
print("변환: {0}".format(arr[2].lower()))
