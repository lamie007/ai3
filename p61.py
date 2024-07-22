score = 80
print ("성적: " + str(score))

x = '토끼'*10
print(x)

n = 100*10
print(n)

i = '100'*20
print(i)

# 200 숫자를 15번 반복해서 출력
n200 = 200
print(str(n200) * 15)

x = '수학성적: '
print(type(x))
y = 80
print(type(y))

date = "20220301"
year = date[0:4]
month = date[4:6]
day = date[6:]
date2 = year + "-" + month + "-" + day
print(date2)

print(len(date))

# 자기이름 핸드폰번호 마지막자리의 갯수 반복하기
name = '김서현'
number = '01025321548'
num = number[-1]
print(num)

res = name *int(num)
print(res)

phone1 = '82-10-4444-4444'

phone2 = '82-02-123-4567'

#조건은 15글자이면 한국 핸드폰 번호 아니면 집번호

n = len(phone1)
i = len(phone2)
print(str(n))
print(str(i))

'''
if n == 15 :
    print( phone1 + '은 한국 번호입니다')
else :
    print( phone1  + '은 집 번호 입니다')

if i == 15 :
    print( phone2 + '은 한국 번호입니다')
else :
    print( phone2  + '은 집 번호 입니다')

'''

if n == 15 and i == 15 :
    print(phone1 , phone2 +'는 한국 번호입니다')
elif n == 15 and i != 15 :
    print(phone1 + '는 한국 번호입니다' , phone2 +'는 집 번호입니다')
elif n != 15 and i == 15 :
    print(phone1 +'는 집 번호입니다' , phone2  + '는 한국 번호입니다')
else:
    print(phone1 , phone2 , '는 집 번호입니다')
