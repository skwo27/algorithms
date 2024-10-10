max = 0
b = 0
for i in range(9):
    a = int(input())
    if a>max:
        max=a
        b = i
print(max)
print(b+1)