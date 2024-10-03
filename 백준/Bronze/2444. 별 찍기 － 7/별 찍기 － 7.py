a = int(input())
for i in range(a):
    print(" "*(a-i-1),'*'*i,'*','*'*i,sep='')
for j in range(a-2,1-2,-1):
    print(" "*(a-j-1),'*'*j,'*','*'*j,sep='')