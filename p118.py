'''a = 'apple'
b = a.upper()
print(b)

height = int(input("키는? "))
weight = int(input("몸무게는?"))

res = (height - 100)*0.9

if res > weight :
    print("다이어트가 필요함")
else :
    print("표준 또는 마른 체형입니다 ")'''

'''print("아르바이트 급여 계산 프로그램")
print(" -주간 근무: 9,500원")
print(" -야간 근무: 주간 시급 * 1.5")

a = int(input("1(주간근무) 또는 2(야간근무) 를 입력해주세요"))
worktime = (int(input("근무 시간을 입력해주세요")))

if a ==1 :
    result = worktime*9500
else :
    result = 9500*worktime*1.5

print("%d시간 동안 일한 급여는 %d원입니다" %(worktime,result))
'''
print("기능선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")


s = int(input("계산기 기능을 선택하세요(1/2/3/4)"))
num1 = int(input("첫 번째 숫자를 입력하세요"))
num2 = int(input("두 번째 숫자를 입력하세요"))

if s== 1:
    print("%d 더하기 %d 는 %d 입니다"%(num1, num2, num1+num2))
elif s == 2:
    print("%d 빼기 %d 는 %d 입니다"%(num1, num2, num1-num2))
elif s == 3:
    print("%d 곱하기 %d 는 %d 입니다"%(num1, num2, num1*num2))
elif s == 4:
    print("%d 나누기 %d 는 %d 입니다"%(num1, num2, num1/num2))