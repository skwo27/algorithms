for i in range(3):
   n = int(input())
   su = 0
   for j in range(n):
      su+=int(input())
   if su>0:
      print('+')
   elif su == 0:
      print('0')
   else:
      print("-")