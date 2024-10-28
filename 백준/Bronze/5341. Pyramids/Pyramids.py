while True:
    b = 0
    a= int(input())
    if a==0:
        break
    for i in range(a,1,-1):
        b+=i
    print(b+1)