# 입력받기 '477569040'
# 입력 받은 문자(숫자)를 1개씩 가져다가 '4'
# 문자를 숫자로 변경한다 '4' -> '4'
# 홀수인지 판단 5 % 2 == 1
# 갯수 세기 cnt = cnt + 1 

'''number =input("숫자를 입력하세요: ")

cnt = 0

for i in number :
    i = int(i)
    if i % 2 == 1 :
        cnt = cnt + 1

print("홀수의 갯수: %d개" %cnt)'''

# 10 20 30 ... 100 출력하기

'''for i in range(5):
    for i in range(10, 101, 10):
        print(i, end=" ")
    print()'''

'''for i in range(5):
    for j in range(5):
        print( i + j + 1, end=" ")
    print()
'''
for i in range(5, 0, -1):
    for j in range( 1, i + 1):
        print( j , end=" ")
    print()