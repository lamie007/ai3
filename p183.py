'''nameList = ['a', 'b']
noList = list(range(34635, 241034))
print(noList)
print(nameList[1])

for i in noList :
    print(i, end=" ")
print()

i = 0
while i < len(noList):
    print( noList[i], end=" ")
    i = i + 1
'''
'''
nameList = ['이순신', '홍길동', '박수연']
nameList[2] = '박수현'
for i in nameList :
    print( i, end=" ")

nameList.insert(1, '이승후') 
print()  
for i in nameList:
    print( i , end= " ")

nameList = ['박수현','이순신', '이승후', '홍길동', '정현희']
searchIndex = nameList.index('박수현' )
print(searchIndex)

member = [1,2,3,4,2,2,2,2]'''

'''p1 = [1,3,5]
p2 = [2,4,6]
p3 = p1 + p2
print(p3)

p4 = list(range(1,11))
print(p4)
p4Sum = sum(p4)
print(p4Sum)

p5 = [100,8,90]
p5Sum = sum(p5)
print(p5Sum)
p5Avg = p5Sum / len(p5)
print( p5Avg)
p5Max = max(p5)
print(p5Max)

p5.reverse()
print(p5)
p5.reverse()
print(p5)

p6 = ['apple', 'banana', 'orange']
print(p6, '!!!')
p6Copy = p6.copy()
p6.remove('apple')
print(p6, '!!!2')
print(p6Copy, '~~~2')

p6Copy[2] = 'manggo'
print(p6Copy)'''

p7 = ['apple', 'banana', 'orange']
p77 = p7
print(p7)
print(p77)

p7.append('bear')
print(p7)
print(p77)

p7.remove('apple')
print(p7)
print(p77)

p77[2] = 'mango'
print(p7)
print(p77)