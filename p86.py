'''year = input("년은?")
month = input("월은?")
day = input("일은?")

print(year, month, day, sep=".")'''

width = int(input("사각형의 너비는?"))
height = int(input("사각형의 높이는?"))

length = 2 * width + 2 * height
area = width * height

print("사각형의 너비: %d cm" %width)
print("사각형의 높이: %d cm" %height)
print("둘레 길이: %d cm" %length)
print("면적: %d" %area)

kg = int(input("킬로그램을 입력하세요 ."))

pound = kg * 2.204623
ons = kg * 35.273962

print("파운드는 %.2f" %float(pound))
print("온스는 %.2f" %float(ons))