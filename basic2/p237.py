# 딕셔너리
member = { 'name' :'황예린', 'age':22 , 'email':'yelin@gmail.com'}
print(member['name'])
print(member['age'])
print(member['email'])

score = dict([('국어', 80), ('영어', 90), ('수학', 100)])
print(score)
print(score['국어'])

score2 = dict([('국어', 80), ('영어', 90), ('수학', 100)])
print(score2)
print(score2['수학'])

score2['국어'] = 90
print(score2, '@@@')
