list1 = [3, 15, -125, '사과', '딸기', True, False]
list2 = list(range(1,21,2))
print(list1)
print(list2)

print(list1[1])

for i in range(7):
    print( list1[6 - i], end=" ")
print('-' *50)
print(list2[9])

list3 = list(range(100, 201, 10))
cnt = 0
sum = 0
for i in list3:
    cnt = cnt + 1
    sum = sum + i
print("리스트의 갯수는 %d" %cnt)
print("합계는 %d" %sum)

# 합계를 구하기
