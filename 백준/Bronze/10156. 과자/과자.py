a,b,c = map(int,input().split())
d = c-a*b
if d >= 0:
    print("0")
else:
    print(abs(d))