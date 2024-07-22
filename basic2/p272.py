def func(n):
    x = n + 5
    return x

a = func(10)
print(a)
b = func(20)
print(b)

def inchToCm(inch):
    cm = inch * 2.54
    return cm

print(inchToCm(10))

def p(n):
    answer = 1
    for i in range(n, 0, -1):
        answer = answer * i
    return answer

print(p(5))
