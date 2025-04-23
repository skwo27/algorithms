import sys

st = [0 for i in range(10001)]
input = sys.stdin.readline
print = sys.stdout.write
for i in range(int(input())):
   s = int(input())
   st[s] += 1
t = 0
for i in st:

    for i in range(i):
        print(str(t) + '\n')
    t+=1