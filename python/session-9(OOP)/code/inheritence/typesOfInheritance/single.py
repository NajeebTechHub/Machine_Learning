class parent:

    def __init__(self,brand,price,camera):
        print('inside parent constructor')
        self.brand = brand
        self.price = price
        self.camera = camera

class child(parent):
    pass


obj = child('oppo',12000,50,'android',2)
print(obj.brand)
print(obj.price)
print(obj.camera)