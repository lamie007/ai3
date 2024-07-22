# 20 22 24 26 ... 50 출력하기

'''cnt = 0
sum = 0
for i in range (20, 51, 2):
    print(i, end=" ")
    cnt = cnt + 1
    sum = sum + i
print()
print("갯수는 %d개" %cnt)
print("숫자의 합게: %d개" %sum)'''

# 100 95 90 ... 0 출력하기
'''
cnt = 0
sum = 0
for i in range (100, -1, -5):
    print(i, end=" ")
    cnt = cnt + 1
    sum = sum + i
    aver = sum / cnt
print()
print("갯수는 %d개입니다" %cnt)
print("합계는 %d입니다" %sum)
print("평균은 : %.2f" %aver)'''

# 1 ~100 까지의 숫자의 합을 구하되 400이 넘으면 멈추기
'''sum = 0
for i in range (1, 101, 1):
    if sum >= 400 :
        break
    sum = sum + i
print("합계는 : %d" %sum)'''

# 200~500 3개 증가하는 수 갯수가 20개일떄 멈추기
'''cnt = 0
for i in range(200, 301, 3):
    if cnt ==20 :
        break
    cnt = cnt + 1
    print(i , end= " ")'''

# 5~ 500 5의 배수 출력 합계가 1000이상이거나 30개 이상이면 멈추기

sum = 0
cnt = 0
for i in range (5, 501, 5):
    print(i , end= " ")
    cnt += 1
    sum += i
    if cnt >= 30 or sum >=1000:
        break
print()   
print("1000이상이거나 30개 이상일때 멈춘 값 : %d %d %d" %(i,cnt,sum))