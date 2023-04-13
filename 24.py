str = open('zadanie24_2.txt').read()
str = str.replace('LDR', 'x')


count, mx = 0, 0
for i in str:
    if i == 'x':
        count+=1
        if mx < count:
            mx = count
    else:
        count = 0

print(mx * 3)