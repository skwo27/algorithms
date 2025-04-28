from sys import stdin,stdout
input = stdin.readline
#print = stdout.write
a = int(input())
arr = []
for i in range(a):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in arr:
    print(i)