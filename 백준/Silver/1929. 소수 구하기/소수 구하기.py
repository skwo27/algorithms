import sys
import math

a, b = map(int, input().split())
ar = []

for i in range(a, b + 1):
    if i < 2:
        continue
    if i == 2:
        ar.append(i)
        continue
    if i % 2 == 0:
        continue
    
    is_prime = True
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        ar.append(i)

sys.stdout.write('\n'.join(map(str, ar)) + '\n')