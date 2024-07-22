# 218~ 222 쪽 풀기

#218
'''questions = [ "s_hool", "compu_er", "deco_ation", "windo_", "hi_tory"]
answers = ['c', 't', 'r', 'w', 's']

for i in range (0, len(questions)):
    q = "%s : 밑 줄에 들어갈 알파벳은?" %(questions[i])
    guess = input(q)

    if guess == answers[i]:
        print("정답!")
    else:
        print("틀렸습니다")
'''
#219
scores = []

while True:
    x = int(input("성적을 입력하세요(종료 시 -1 입력): "))

    if x == -1 :
        break
    else:
        scores.append(x)

sum = 0
for score in scores:
    sum = sum + score

avg = sum / len(scores)
print("합계는: %d , 평균: %.2f" %(sum, avg))

#220 