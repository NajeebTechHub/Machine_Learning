class MyAtm:

    def __init__(self):
        self.pin = ''
        self.__balance = 0


    def get_balance(self):
        return self.__balance
    
    def set_balnce(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('given input is not integer')

    



obj = MyAtm()

print(obj.get_balance())
print(obj.set_balnce(100))
print(obj.get_balance())