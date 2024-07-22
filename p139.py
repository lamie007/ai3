hour1 = int(input("첫 번째 시간의 시를 입력하세요"))
minute1 = int(input("첫 번째 시간의 분을 입력하세요"))

hour2 = int(input("두 번째 시간의 시를 입력하세요"))
minute2 = int(input("두 번째 시간의 분를 입력하세요"))

if hour1 > hour2 :
    print("늦은 시간 : %d:%d" %(hour1,minute1))
    print("빠른 시간 : %d:%d" %(hour2,minute2))
elif hour1 == hour2 and minute1 < minute2:
    print("빠른 시간 : %d:%d" %(hour1,minute1))
    print("늦은 시간 : %d:%d" %(hour2,minute2))
elif hour1 == hour2 and minute1 > minute2:
    print("빠른 시간 : %d:%d" %(hour2,minute2))
    print("늦은 시간 : %d:%d" %(hour1,minute1))
elif hour1 < hour2:
    print("빠른 시간 : %d:%d" %(hour1,minute1))
    print("늦은 시간 : %d:%d" %(hour2,minute2))

num1 = hour1*100 + minute1
num2 = hour2*100 + minute2

if num1 > num2 :
    res = num1 - num2
    print("%d:%d가 %d:%d보다 %d분 더 빠르다" %(hour2,minute2,hour1,minute1,res))
elif num2 > num1 :
    res = num2 - num1
    print("%d:%d가 %d:%d보다 %d분 더 빠르다" %(hour1,minute1,hour2,minute2,res))