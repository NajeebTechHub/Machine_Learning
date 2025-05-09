class parent:

    def __init__(self,brand,price,camera):
        print('inside parent constructor')
        self.brand = brand
        self.price = price
        self.camera = camera

class child(parent):

    def __init__(self,brand,price,camera,os,ram):
        print('inside child constructor')
        super().__init__(brand,price,camera)
        self.os = os
        self.ram = ram
        print('inside child  constructor')


obj = child('oppo',12000,50,'android',2)
print(obj.brand)
print(obj.price)
print(obj.camera)
print(obj.os)
print(obj.ram)