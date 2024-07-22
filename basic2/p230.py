animals = ('토끼', '거북이', '사자', '여우')
print(animals)

numbers = tuple(range(10))
print(numbers)

#출력하기
print(animals[1])
print(numbers[3])

# animals[2] = '호랑이' 튜플은 수정 불가 

anNu = animals + numbers
print(anNu)