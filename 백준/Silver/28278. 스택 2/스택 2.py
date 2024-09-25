import sys
input = sys.stdin.readline
print = sys.stdout.write
steck = []
for i in range(int(input().strip())):
    a = str(input().strip())

    if a.split()[0] == "1":
        steck.append(int(a.split()[1]))
    elif a == "2":
        if steck ==[]:
            print('-1'+'\n')
        else:
            print(str(steck[-1])+'\n')
            del steck[-1]
    elif a == "3":
        print(str(len(steck))+'\n')
    elif a == "4":
        if steck == []:
            print('1'+'\n')
        else:
            print('0'+'\n')
    elif a == "5":
        if steck == []:
            print('-1'+'\n')
        else:
            print(str(steck[-1])+'\n')