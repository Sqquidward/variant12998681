file = open('26.txt')

n = int(file.readline())
list = []
for i in range(n):
    list.append(int(file.readline()))

count, mx = 0, 0
for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        if ((list[i] % 2 == 0 and list[j] % 2 == 0) or (list[i] % 2 != 0 and list[j] % 2 != 0)) and (list[i] + list[j]) in list:
            count += 1
            mx = max(mx, list[i] + list[j])
print(count, mx)



