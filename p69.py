"""
name = input('이름을 입력하세요')
"""

"""age = input('당신의 나이는?')
print("당신의 나이는 %d살입니다"%int(age))
"""

'''date = input('당신이 태어난 연도는?')
age = 2024-int(date)
print("당신의 나이는 %d살입니다" %int(age))
'''
# 73

'''a = input("첫 번째 정수를 입력하세요: ")
b = input("두 번째 정수를 입력하세요:")
c = a+ b
print(c)

a = input("첫 번째 정수를 입력하세요: ")
b = input("두 번째 정수를 입력하세요:")
c = int(a)+ int(b)
print(c)'''

'''a = input("첫 번째 정수를 입력하세요: ")
b = input("두 번째 정수를 입력하세요:")

if a > b :
    print("큰 숫자는 %d 입니다"%int(a))
else print("큰 숫자는 %d 입니다"%int(b))
 '''
a = input("첫 번째 정수를 입력하세요: ")
b = input("두 번째 정수를 입력하세요:")
c = input("세 번째 정수를 입력하세요")

if a > b and a > c :
    print("큰 숫자는 %d 입니다"%int(a))
elif b > a and b > c:
    print("큰 숫자는 %d 입니다"%int(b))
else :
     print("큰 숫자는 %d 입니다"%int(c))
