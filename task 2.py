def f(x, y, z, w):
    return (x or not(y)) and not(w == z) and w


print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w, f(x, y, z, w))

#wzyx