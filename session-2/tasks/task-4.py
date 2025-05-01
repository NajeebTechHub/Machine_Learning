# Problem 4: Write a menu-driven program -
# cm to ft
# km to miles
# USD to INR
# exit
while True:
   print('''
   1:cm to ft
   2:km to miles
   3:USD to PKR
   4:exit
   ''')
   choice = int(input('Enter your choice in number : '))
   result = 0
   if choice == 1:
     cm = float(input('Enter your value in cm : '))
     result = cm / 30.48
     print(f'{cm}cm is = {result}ft')
   elif choice == 2:
     km = float(input('Enter your value in km : '))
     result = km / 1.621
     print(f'{km}km is = {result}miles')
   elif choice == 3:
     USD = float(input('Enter your value in USD : '))
     result = USD * 278.21
     print(f'${USD} is = {result}PKR')
   elif choice == 4:
     break
   else:
     print('Invalid choice')