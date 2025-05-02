st = input('Enter your string = ')

count = 0
for i in range(0,len(st)):
    if st[i] == ' ':
        count = count + 1
print('your string is of',count + 1,'words')