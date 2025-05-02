s = input('Enter a string = ')

flag = True
for i in range(0,len(s)//2):
    if s[i] != s[len(s) - i - 1]:
        print('The string is not palindrome')
        flag = False
        break
if flag:
    print('The string is palindrome')