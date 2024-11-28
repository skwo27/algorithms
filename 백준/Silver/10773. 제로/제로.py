total = []
for i in range(int(input())): 
   a = int(input())
   if a == 0: 
      total.pop(-1)
   else: 
      total.append(a)
print(sum(total))