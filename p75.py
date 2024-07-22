year = 2024
month = '07'
day = 12
print(year, month, day, sep="/")

price = 1000
print(price, "원", sep="")

print("안녕하세요\n 반갑습니다")
print("안녕하세요\t 반갑습니다")
print("\\")
print("\'")
# 안녕
print("\'안녕\'")

kor = input("국어성적을 입력하세요")
eng = input("영어성적을 입력하세요")
mat = input("수학성적을 입력하세요")

sum = int(kor) + int(eng) + int(mat)
aver = int(sum) / 3

print("총 합:" ,int(sum))
print( "평균:" ,float(aver))