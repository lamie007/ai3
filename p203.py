'''data = [ 12, 8, 15, 69, 43, 54, 76]
print(data)
data.sort()
print(data)

data2 = [ 'a', '가', '@', 1, 'ac']
data.sort(reverse=True)
print(data2)

data2.sort(reverse=False)
print(data2)
'''
'''string1 = "사과는 맛있다, 나는 사과를 제일 좋아한다"
print(string1)

x = string1[0].replace("사과", "딸기", -1)
string1 = [x]
print(string1)

hello = 'have a nice day'
print(hello)

list1 = hello.split(" ")
print(list1)
print(type(list1))

for i in range(0, len(list1)):
    print("list1[%d] : %s" %(i, list1[i]))
'''
list1 = 'a,b,c,d,e,f'

list1= list1.split(',')
print(list1)

#출력은 홍길동 
list2 = ['홍길동:100:20', '이순신:90:80', '최수연:100:75']
list22 = list2[0]
list22 = list22.split(':')
print(list22[0])

list22 = []
for i in list2:
    list10 = i.split(':')
    print(list10)
    for j in list10 :
        list22.append(j)
print(list22)

list5 = ['kbs-사장-200, mbc-부장-100','kbs-사원-50, sbs-대리-80']

list51 = list5[0].split(',')
list51 = list5[1].split(',')
for i in list5:
    list51 = i.split("-")
    print(list51)

import requests as req
url = "http://search.naver.com/search.naver"
rData = req.get(url, params={'query' : '백일해 증상'}) 
print(rData.text)

names = [ 'a', 'b', 'c']
x = '-'.join(names)
print(x)

list2D = [ [1,2], [3,4,5], [1] ]
print(list2D[1][1])
print(list2D[0][1])

list2DD = [ [1,2,3,4], [5,6,7]]

for i in range(0, len(list2DD)):
    for j in range ( 0, len(list2DD[i])) :
        print(list2DD[i][j], end=" ")
    print()

list3D = [[ [1,2,3], [4,5]], [ [6,7], [8]]]
# 8을 출력
print(list3D[1][1][0])
# 1을 출력
print(list3D[0][0][0])
