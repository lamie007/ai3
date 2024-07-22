num = input("수를 입력하세요")
res = len(num)


if res ==1 :
    print("%s는 한자리 숫자입니다"%num)
elif res ==2:
    print("%s는 두자리 숫자입니다"%num)
elif res ==3:
    print("%s는 세자리 숫자입니다"%num)
else:
    print("오류! %s는 범위(0~999)이외의 숫자이다"%num)

