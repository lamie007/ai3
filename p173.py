# 173
'''n = 1 
sum = 0
count = 0

while n <= 100:
    if n % 2 == 1:
        sum = sum + n
        print("%6d" %sum, end=" ")
        count = count + 1
    if count % 10 == 0 :
        print()
    n = n + 1'''

# 174
'''dollar = 10

while dollar <= 100:
    won = dollar *1080
    euro = dollar * 0.81

    print("%3d %8.0f %7.1f" %(dollar,won,euro))

    dollar = dollar + 10
'''
# 175
sentence = input("문장을 입력하세요")
i = len(sentence) - 1

while i >= 0:
    if sentence[i] == " ":
        print("-", end= " ")
    else:
        print("%s" %sentence[i], end=" ")
    i = i -1

