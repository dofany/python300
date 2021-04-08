# 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0

nums = [1,2,3,4,5]
sum = 0
avg = len(nums)
for i in nums:
    sum = sum+i
print(sum/avg)