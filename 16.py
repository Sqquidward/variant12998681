def F(n):
    if n == 1:
        return 2
    elif n >= 2:
        return F(n-1)

print(F(5))