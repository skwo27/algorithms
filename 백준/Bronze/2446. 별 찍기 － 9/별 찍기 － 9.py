a = int(input())
for i in range(a):
    print(" "*i,'*'*(2*a-2*i-1),sep='')
for j in range(1,a):
    print(" "*(a-j-1),"*"*j,'*',"*"*j,sep='')