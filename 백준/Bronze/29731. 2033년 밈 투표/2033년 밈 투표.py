dic = [
"Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

t = True

for i in range(int(input())):
    a = str(input())
    if a not in dic:
        t = False

if t==True:
    print('No')
else:
    print('Yes')