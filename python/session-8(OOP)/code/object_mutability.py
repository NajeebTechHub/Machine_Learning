class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# function outside the class
def greet(person):
    person.name = 'haseeb'
    return person

p = Person('najeeb','male')
print(id(p))
p1 = greet(p)
print(id(p1))

# the both are same because the object by default is mutable
# if you make it immutable then the address will be change
