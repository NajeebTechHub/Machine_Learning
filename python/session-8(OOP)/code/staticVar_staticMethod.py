class Atm:

    # static variable
    # counter = 1
    __counter = 1

    def __init__(self):
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter + 1

    @staticmethod
    def get_counter():
        return Atm.__counter
    


print(Atm.get_counter())

obj1 = Atm()
print(obj1.cid)


obj2 = Atm()
print(obj2.cid)

obj3 = Atm()
print(obj3.cid)