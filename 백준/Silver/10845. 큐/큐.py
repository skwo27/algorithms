steck = []
for i in range(int(input())):
    a = str(input())

    if a.split()[0] == "push":
        steck.append(int(a.split()[1]))
    elif a == "pop":
        if steck ==[]:
            print(-1)
        else:
            print(steck[0])
            del steck[0]
    elif a == "size":
        print(len(steck))
    elif a == "empty":
        if steck == []:
            print(1)
        else:
            print(0)
    elif a == "back":
        if steck == []:
            print(-1)
        else:
            print(steck[-1])
    elif a == "front":
        if steck == []:
            print(-1)
        else:
            print(steck[0])