# 160~ 164 까지 풀어보기 

#160
'''a = 2

for b in range (1, 10):
    print("%d X %d = %d" %(a,b,a*b))'''

#161
'''for a in range (2, 10):
    for b in range (1, 10):
        print("%d X %d = %d" %(a, b, a*b))'''

#163   
for i in range (0 , 4):
    for j in range (0, 9):
        print("*",end=" ")
    print()

#164

for i in range (9, 0, -1):
    for j in range (j , i + j):
        print(i, end=" ")
    print()