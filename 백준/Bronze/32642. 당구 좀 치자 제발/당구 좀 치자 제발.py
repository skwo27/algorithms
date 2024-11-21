n = input()
l = list(map(int,input().split()))
summ = 0
an  =0
for i in (l):
   if i == 1:
      an +=1 
      summ+= an
   else:
      an-=1
      summ+=an
print(summ)