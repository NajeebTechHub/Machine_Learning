class parent:

    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class child(parent):

    def __init__(self,num,val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val
    
obj = child(100,200)
print(obj.get_num())
print(obj.get_val())