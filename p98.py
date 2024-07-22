'''x = 10
if x > 0 :
    print("양수")

y = 100
if y>=90 :
    print("A+")
else :
    print("낮은 점수")'''

'''score = int(input("점수를 입력하세요"))

if score >= 90 :
    print("A+")
elif score >= 80 :
    print("B+")
elif score >= 70 :
    print("C+")
elif score >= 60 :
    print("D+")
else:
    print("F")'''

score1 = 75
score2 = 90
print( score1 >= 80 and score2 >= 80)
print( score1 >= 80 or score2 >= 80)

x = 10
print( x%2 ==0 or x%6 == 0)
print ( not( x != 10))

'''# 105 1 
a = 5
b = 7
c = a+b
print(c==12)
# 2 
hobby1 = "영화감상"
hobby2 = "수영"
my_hobby = "독서"
print (my_hobby == hobby1 or my_hobby == hobby2)
# 3 
pilgi = 90
silgi = 70
print (pilgi >= 80 and silgi >=80)
'''

age = int(input("나이는?"))

if age >=65 :
    print("입장료는 무료입니다")
elif age >=10 and age <=20 :
    print("입장료는 1500원입니다")
elif age >=5 and age <=9:
    print("입장료는 1200원입니다")
elif age >=0 and age <= 4:
    print("입장료는 1000원입니다")

