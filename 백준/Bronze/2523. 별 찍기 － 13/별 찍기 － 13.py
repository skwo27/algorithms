a = int(input())
for i in range(1,a+1):
    print("*" * i,sep="")

for j in range(a):
    print("*" * (a-j-1),sep="")