# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
#
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# 출력 예시:
# 6700

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800,
            '월드콘': 1500, '메로나': 1000}
a = list(icecream.values())
print(sum(a))