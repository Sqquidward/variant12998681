def f(i, n):
    if i >= 50 and n == 2:
        return True
    elif i < 50 and n == 2:
        return False
    elif i >= 50 and n > 2:
        return False
    else:
        if n % 2 == 0:
            return f(i + 1, n + 1) and f(i + 2, n + 1) and f(i * 2, n + 1)
        else:
            return f(i+1, n+1) or f(i+2, n+1) or f(i*2, n+1)


for i in range(1, 50):
    if f(i, 0):
        print(i)
        break