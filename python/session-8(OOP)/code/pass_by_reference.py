class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# function outside the class
def greet(person):
    print(id(person))
    print('Hello ',person.name,'Your gender is ',person.gender)
    p1 = Person('haseeb','male')
    return p1

p = Person('najeeb','male')
# pass the reference of object as argument
# p is not an object it is a reference(address) of Person() object
greet(p)

# the id of p and person parameter of greet is same
print(id(p))

# a function can return an object of the class
x = greet(p)
print(x)