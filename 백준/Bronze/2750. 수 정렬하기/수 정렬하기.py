import sys
a = int(sys.stdin.readline())
b = []
for i in range(a):
    c = list(map(int,sys.stdin.readline().split(" ")))
    b = (b+c)
b = list(b)
b.sort()
for j in b:
    sys.stdout.write(str(j) + '\n')