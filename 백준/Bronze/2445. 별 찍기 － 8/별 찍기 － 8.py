a = int(input())
for i in range(1,a+1):
    print('*'*i," "*(a*2-i*2),'*'*i,sep='')
for j in range(a-1,0,-1):
    print('*'*j," "*(a*2-j*2),'*'*j,sep='')