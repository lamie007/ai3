# while 조건식 :
#       참이면 수행하는 문장
# 조건식 거짓이면 처리
# 또는 조건식 다음으로 처리

# 1 ~ 10까지 합계 구하기
'''i = 1
sum = 0
while i <= 10 :
    sum = sum + i
    i = i + 1
print("합계는 %d" %sum)'''

# 500 ~600 까지의 정수 중 5의 배수 합계를 구하는 프로그램
'''i = 500
sum = 0
while i <=600 :
    if i % 5 == 0 :
        sum = sum + i
    i = i + 1
print("합계는 %d" %sum)'''

# 1 ~1000 까지 정수 중 100의 배수를 제외하고 합계를 구하기

'''i = 1
sum = 0
while i <= 1000:
    if not(i % 100== 0) :
        sum = sum + i
    i = i + 1
print("합계는: %d" %sum)
''''''
s = "Python is widely used by a number of big companies"
i = 0
count = 0'''

'''print("모음 : ", end=" ")
while i <= len(s)-1 :
    if (s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E'
       or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O'
       or s[i] == 'u' or s[i] == 'U'):
        count = count + 1
        print(s[i], end=" ")
    i = i +1
print()
print('모음 갯수: %d'%count)'''

# 숫자 두개를 입력 받아서 덧셈하기

'''button = "y"
while button == "y" or "Y":
    num1 = int(input("첫 번째 숫자를 입력하세요"))
    num2 = int(input("두 번째 숫자를 입력하세요"))
    sum = num1 + num2
    print("합계는: %d" %sum)
    button = input("계속 하시겠습니까? ( y:계속 n:그만)")'''

# 문자열을 2개 입력 받아서 합치기
# 예 문자1 : Hello
#    문자2 : Love
#   출력 결과 : H L e o l v l e o 
# 계속 하시겠습니까? (y/n)

'''button = "y"
sum = ""
i = 0
j = 0

while (button == "y"):
    str1 = input("첫 번째 영어 문자열을 입력하세요")
    str2 = input("두 번째 영어 문자열을 입력하세요")
    while i < len(str1) or j < len(str2):
        if  i <= len(str1) - 1:
            sum = sum + str1[i]
            i = i + 1
        if j <= len(str2) -1 :
            sum = sum + str2[j]
            j = j + 1
    print(sum)
    
    button = input("계속 하시겠습니까? (y:계속 n:그만)")
'''

'''yN = "y"
while( yN=="y" ) :
    w=input("문자1 : " )
    s=input("문자2 : ")
    ws = ""
    for i in range( len(w) + len(s)) : # 0, 1, 2, .... 8
        if i <= len(w)-1 : # i<=4 0, 1, 2, 3, 4
           ws = ws + w[i]
        if i <= len(s)-1 : # i<=3 0, 1, 2, 3 
           ws = ws + s[i]
    print(ws)
    yN = input("계속하실래요?(y/n)")'''