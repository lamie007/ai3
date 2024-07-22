'''word = "I am Happy"

for i in word:
    print(i , end="")
'''

'''phone = "010-1234-2284"
print(phone)

# 핸드폰 번호안에 5가 있는지
a = False

for i in phone:
    if i == "5":
        print("있습니다")
        a = True
        break
else:
    print("없습니다")'''

#영어 문장에 'a'가 있는지

word = "apple"

cnt = word.count("a")
ans = False
for i in word:
    if i == "a":
        ans = True 
        print("%d개 있어요" %cnt)
        break
else:
    print("없습니다")

'''for i in word:
    if i == "a":
         flag = 1
         cnt += 1
    if flag == 0:
        print("a가 없어요")
    else:
        print("%d개 있습니다" %cnt)

        '''

for j in range(0,3,1):
    word = input("영어 단어는?")
    flag = 0 
    cnt = 0
    for i in word :
        if i == 'a':
            flag=1
            cnt +=1
        if flag == 0:
            print("a가 없음")
        else:
            print("%d개 있습니다" %cnt)