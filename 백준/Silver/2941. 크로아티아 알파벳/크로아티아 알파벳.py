a = str(input())
q = len(a)
b = a.count('c=')
q-=b*2
c = a.count('c-')
q-=c*2
d = a.count('dz=')
q-=d*2
e = a.count('d-')
q-=e*2
f = a.count('lj')
q-=f*2
g = a.count('nj')
q-=g*2
h = a.count('s=')
q-=h*2
i = a.count('z=')
q-=i*2
p = b+c+d+e+f+g+h+i
print(p+q)