import math
a = int(input())
f = True
if a<10 : 
    print('NO')
    f = False
else:
    for i in range(len(str(a))):
        b = str(a)[:i+1]
        c = str(a)[i+1:]
        b1 = list(b)
        c1 = list(c)
        b1 = list(map(int, b1))
        c1 = list(map(int, c1))
        if math.prod(b1) == math.prod(c1):
            print('YES')
            f = False
            break
if f != False:
    print('NO')