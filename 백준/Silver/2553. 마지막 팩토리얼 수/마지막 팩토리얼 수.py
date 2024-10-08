import math
import sys
a = int(sys.stdin.readline())
a = math.factorial(a)
a = str(a)
alist = list(a)
alist.reverse()
for i in alist:
    if i != '0':
        print(i)
        break