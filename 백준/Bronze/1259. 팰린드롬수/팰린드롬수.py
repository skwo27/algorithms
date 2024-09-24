while True:
   a = str(input())
   b = 0
   if a =='0':
      break
   for i in range(len(a)//2+1):
      if a[i] != a[(i+1)*-1]:
         b  +=1
   if b == 0: print('yes')
   else: print('no')