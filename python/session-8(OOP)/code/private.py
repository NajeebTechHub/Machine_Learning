class MyAtm:

    def __init__(self):
        self.pin = ''
        self.__balance = 0
        # self.menu()


    def menu(self):
        user_input = input('''
            Welcome Here!
            How i can help you?
            1. Enter 1 for create pin
            2. Enter 2 for change pin
            3. Enter 3 for check balance
            4. Enter 4 for withdraw balance
            5. Anything else exit
            ''')
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw_balance()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Create a pin ')
        self.pin = user_pin

        user_balance = int(input('Enter balance for deposit '))
        self.__balance = user_balance

        print('pin created sucessfully')


    def change_pin(self):
        old_pin = input('Enter your old pin ')
        if old_pin == self.pin:
            new_pin = input('Enter new pin ')
            self.pin = new_pin
            print('pin successfully changed')
        else:
            print('old pin is not correct')

    
    def check_balance(self):
        user_pin = input('Enter your pin ')
        if user_pin == self.pin:
            print('Your account balance is : ',self.__balance)
        else:
            print('incorrect pin')



    def withdraw_balance(self):
        user_pin = input('Enter your pin ')
        if user_pin == self.pin:
            amount = int(input('Enter amount : '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('Successfully withdraw')
                print('your account balance is : ',self.__balance)
            else:
                print('insufficient balance')



obj = MyAtm()
obj.create_pin()
# change the vairable value
# obj.balance = 'hehehe'

# can't effect the code because it create new variable
# obj.__balance = 'hehehe' 

# after private you can't access and shange the variable like this
obj._MyAtm__balance = 'hehehe' 

obj.withdraw_balance()