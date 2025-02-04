input()
w = input()
l = list(map(int,input().split()))
l2 = list(map(int,input().split()))
loser = []
for i in l2:
    for j in range(1,i):
        l.append(l[0])
        del l[0]
    loser.append(l[0])
print(*loser)