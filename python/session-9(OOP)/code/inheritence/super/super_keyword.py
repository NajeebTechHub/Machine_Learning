class parent:
    
     def __init__(self,name,age):
          self.name = name
          self.age = age

     def buy(self):
          print('parent buy phone')


class child(parent):
     
     def buy(self):
          print('child by phone')
          super().buy()


obj = child('najeeb',23)
obj.buy()
