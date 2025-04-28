import math

A,B,V = map(int,input().split())
# t = 0
# d = 1
# while True:
#     t+=A
#     if t >= V:
#         break
#     else:
#         t-=B
#     d+=1
# print(d)


# A + d(A+B) = V
print(math.ceil((V-A) / (A-B)) +1)
