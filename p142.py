'''for x in range(5) :
    print(x)
    print("Hello")
'''
'''sum = 0
for i in range(1,101,2) :
    print( i )'''

'''sum = 0 
for i in range(1,11,1) :
    print(i)
'''
'''sum = 0
for i in range(0,11, 2) :
    sum = sum + i
    print("i의 값: %d=>합계:%d"%(i, sum))

for i in range(10):
    print(i, end=" ")
print()'''
'''
# 5 10 15 20 ... 100
for i in range(5, 101, 5):
    print(i, end=" ")

# 4 8 12 16 ... 200
for i in range(4, 201, 4 ):
    print(i, end=" ")
'''
#200 150 100 50 0 -50 -100 -150 -200

for i in range(200, -201, -50):
    print(i, end= " ")

cnt = len(range(200, -201, -50))

print("%d개입니다" %cnt)

cnt = 0
for i in range(5, 101, 5):
    print(i, end=" ")
    cnt = cnt + 1
print()
print("갯수는: %d"%cnt)