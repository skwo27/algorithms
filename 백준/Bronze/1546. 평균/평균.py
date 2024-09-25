p = int(input())
arr = list(map(int,input().split()))
m = max(arr)
b = 0
for i in arr:
    b+=i/m*100
print(b/p)