import sys
a = int(input())
for i in range(a):
    a = list(map(int,sys.stdin.readline().split()))
    a.sort()
    print(a[-3])