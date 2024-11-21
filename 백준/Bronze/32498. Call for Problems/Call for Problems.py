s = 0
n = int(input())
l = list()
for i in range(n):
   l.append(int(input()))
for i in l:
   if i%2!=0:
      s+=1
print(s)