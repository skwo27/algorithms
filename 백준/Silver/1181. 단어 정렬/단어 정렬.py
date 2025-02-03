li=[]
for i in range(int(input())):
    li.append(input())
li2 = set(li)
li = list(li2)
li.sort()	
li.sort(key=len)


for i in li:
    print(i)