a = int(input())
print(" "*(a-1),"*",sep="")
for i in range(1,a):
	print(" "*(a-i-1),'*'*(1+2*i),sep="")