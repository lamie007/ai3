'''def hello() :
    print('hello')

for i in range(20):
    hello()

# 1 ~ 100까지 합계 구하기 함수 정의하기
def uSum() :
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)

def hype():
    print('-'*50)

# 만들어진 함수를 사용하는 쭉-비지니스로직
uSum() #함수 호출
uSum() #함수 호출
print('-' *50)

for i in range(1, 101):
    if sum >= 3000 :
        break
    sum = sum + i
print('3000 이상일 때 항목의 %d 값 합계 : %d' %(i, sum))

def iSum():
    sum = 0
    for i in range(1, 101):
        if sum >= 3000 :
            break
        sum = sum + i
    print('3000 이상일 때 항목의 %d 값 합계 : %d' %(i, sum))
'''

start = int (input("시작 수 :"))
end = int (input("끝 수 :"))

def addSum( ustart, uend):
    sum = 0
    for i in range(ustart, uend+1):
        sum = sum + i
    print("합계는 : %d" %sum)

addSum(start, end)