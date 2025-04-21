ar=[]
from sys import stdin
input = stdin.readline
for i in range(int(input())):
    ar.append(float(input()))
for i in range(7):
    print("%.3f" %min(ar))
    ar.remove(min(ar))