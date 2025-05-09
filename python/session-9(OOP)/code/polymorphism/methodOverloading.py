class parent:

    def area(self,a,b=0):
        if b == 0:
            return 3.14 * a * a
        else:
            return a * b

p = parent()
print(p.area(2))
print(p.area(2,5))
