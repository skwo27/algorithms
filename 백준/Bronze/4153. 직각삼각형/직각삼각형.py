while True:
   ar  = list(map(int,input().split()))
   c = max(ar) 
   ar.remove(c)
   b = max(ar)
   a = min(ar)
   if a == b == c and a==0:
      break
   if a**2 +b**2 == c**2:
      print("right")
   else:
      print('wrong')