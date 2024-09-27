a = input()
arr = list(map(int,input().split())) 
c = 0
for i in arr:
    t = 0
    if i == 1 or i != 2 and i % 2 == 0:
        continue
    else:
        for j in range(2,i-1):
            if i%j==0:
                t+=1
        if t==0: c+=1
print(c)