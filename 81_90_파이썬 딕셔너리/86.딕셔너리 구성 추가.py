# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
#
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500

icecream = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
icecream.update({"죠스바":1200,"월드콘":1500})
print(icecream)
print(type(icecream))

# icecream = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
# icecream["죠스바"]=1200
# icecream["월드콘"]=1500
# print(icecream)
# print(type(icecream))