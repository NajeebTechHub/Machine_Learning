lower = int(input("Enter lower number = "))
upper = int(input("Enter upper number = "))

for i in range(lower,upper):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)    