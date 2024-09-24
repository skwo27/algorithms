x,y,w,h = map(int,input().split())

ar = [x,y,w-x,h-y]
print(min(ar))