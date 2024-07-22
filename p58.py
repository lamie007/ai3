s = "안녕하세요 반갑습니다."
print(s)
print( s[0] + s[1])
print( s [ 0 : 3 ] )
print ( s [ 7 : 10 ])

string = '쥐 구멍에 볕들 날 있다'
print(string[2:8])

animal = 'tiger'
print(animal[0:2])

jumin = '991013-463486'
# 99년 10월 13일
print(jumin[0:2] +'년' , jumin[2:4] +'월', jumin[4:6] +'일')

sex = jumin[7]
print( sex )

# 1 , 3 인 경우 남자 출력 2, 4인 경우 여자 출력
if sex == '1' or sex=='3' :
    print("남자")
else :
    print("여자")

# 주민번호 제일 마지막 부분에 짝수이면 맞는 주민번호 출력
# 홀수이면 '틀린 주민번호' 출력

num = jumin[12]

num = int(num)

if num % 2 == 0 :
    print('맞는 주민번호')
else :
    print('틀린 주민번호')

end = jumin[-1]
print( end)