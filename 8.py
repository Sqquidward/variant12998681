from itertools import product

count = 0
for i in product('ПИР', repeat = 5):
    if i.count('П') == 1:
        count += 1
print(count)