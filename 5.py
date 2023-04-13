def f(n):
    n_2, sum = bin(n)[2:], 0
    for elem in str(n_2):
        sum += int(elem)
    return int(n_2 + str(sum % 2), 2)

for i in range(1000):
    if f(f(i)) > 93:
        print(f(f(i)))
        break
