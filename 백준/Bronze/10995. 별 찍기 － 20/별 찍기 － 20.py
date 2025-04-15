a = int(input())
b = 0
for i in range(a):
    b+=1
    if b%2==0:
        print(' ',end = '')
    print('* '*a)