import sys 
input = sys.stdin.readline

p = int(input())
arr = []

for i in range(p):
    arr.append(int(input()))
for i in sorted(arr):
    print(i,end='\n')
