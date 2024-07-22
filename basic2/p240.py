words = {'door':'문', 'chair':'의자', 'table':'책상', 'house': '집'}
print(words)

words["table"] = '테이블'
print(words)

words['house'] = '하우스'
print(words)

car = {"brand": "혅대", "model":"아반떼", "start": "1990", "year": "2021"}
print(car)

x = car.pop("start")
print(x)

print(car)

car.clear
print(car)

area_code = {"서울":"02", "부산":"051", "대구":"053", "광주": "062"}

for key in area_code:
    print("%s 지역번호 : %s" %(key, area_code[key]))

scores = { "김채린" : 85, "박수정": 98, "함소희": 94, "안예린": 90, "연수진":93}

sum = 0

for key in scores:
    sum = sum + scores[key]

print("%s : %d" %(key, scores[key]))

avg = sum / len(scores)

print("합계: %d 평균: %.2f" %(sum, avg))

admin = {"id":"admin", "password": "12345"}

input_id = input("아이디를 입력하세요")
input_pass = input("비밀번호를 입력하세요")

if input_id == "admin" and input_pass == "12345":
    print("정보에 접근 권한이 있습니다")
else:
    print("접근 권한이 없습니다")

