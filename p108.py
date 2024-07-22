# 배수 
'''num = int(input("숫자를 입력하세요"))
# result = "3의 배수도 4의 배수도 아니다"

if num %2 ==0 and num %4 ==0:
    print("행운의 수")
elif num ==3 :
    print(num)
else :
    print("입력받는 수 ")'''

# 영어 단어 퀴즈
'''ans = input("사자의 영어 단어는 무엇일까요??")
result = "땡 틀렸습니다"

if ans == "lion":
    result = "정답입니다"
print(result)'''

'''start = int(input("시작 수는?"))
end = int(input("끝 수는?"))
num = int(input("정수를 입력하세요"))

if num < end and num > start :
    print("%d와 %d 사이입니다"%(start,end))
else :
    print("%d와 %d 사이가 아닙니다"%(start,end))
'''
#월 입력받아 계절 출력
'''month = int(input("월을 입력하세요"))

if month >= 3 and month <= 5 :
    print("%d월은 봄입니다" %month)
elif month >= 6 and month <= 8 :
    print("%d월은 여름입니다" %month)
elif month >= 9 and month <= 10 :

    print("%d월은 가을입니다" %month)
else:
    print("%d월은 겨울입니다" %month)'''

#주민번호 뒷자리 입력받아 남여 판정
num = int(input("주민번호 뒷자리 첫 번째 숫자를 입력하세요"))

if num == 2 or num == 4 :
    print("여자입니다")
elif num == 1 or num == 3 :
    print("남자입니다")
else:
    print("다시 입력하세요")