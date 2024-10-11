a = int(input())
b = int(input())
c = int(input())
d = a*b*c
for j in range(0,10):
    p = 0
    for i in str(d):
        if str(j) == i:
            p+=1
    print(p)