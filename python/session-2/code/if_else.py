email = "anjumnajeeb@gmail.com"
password = "6789"

inputemail = input("Enter your email = ")
inputpsd = input("Enter your password = ")

if inputemail == email and inputpsd == password:
    print("Welcome " + email)
else:
    print("wrong email or password")    