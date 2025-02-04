p,a = map(int,input().split())
l = list(map(int,input().split()))


if a < sum(l):
    for i in range(len(l)):
        a-=l[i]
        if a<0:
            an = i +1
            break
        if a<=0:
            an = i +2
            break
else:
    l.reverse()
    a-=sum(l)
    for i in range(len(l)):
        a-=l[i]
        if a<=0:
            an = p - i
            break
print(an)