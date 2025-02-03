a,b = map(int,input().split())
l = []
for i in range(a+b):
    for j in range(i):
        l.append(i)
print(sum(l[a-1:b]))