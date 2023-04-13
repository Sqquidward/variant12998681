alp = '01234567'

mn = 100**10
for x in alp:
    if x == '0':
        continue
    for y in alp:
        ans = int(f'{x}01{y}4', 9) + int(f'{x}{y}544', 8)
        if ans % 89 == 0:
            mn = min(mn, ans//89)
print(mn)
