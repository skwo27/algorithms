a = int(input())
for i in range(1,a+1):
    print(" "*(a-i),"*" * i,sep="")

for j in range(a):
    print(' '," "*j,"*" * (a-j-1),sep="")