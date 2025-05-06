class MyAtm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()


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
        self.balance = user_balance

        print('pin created sucessfully')

        self.menu()

    def change_pin(self):
        old_pin = input('Enter your old pin ')
        if old_pin == self.pin:
            new_pin = input('Enter new pin ')
            self.pin = new_pin
            print('pin successfully changed')
        else:
            print('old pin is not correct')
        
        self.menu()
    
    def check_balance(self):
        user_pin = input('Enter your pin ')
        if user_pin == self.pin:
            print('Your account balance is : ',self.balance)
        else:
            print('incorrect pin')

        self.menu()

    def withdraw_balance(self):
        user_pin = input('Enter your pin ')
        if user_pin == self.pin:
            amount = int(input('Enter amount : '))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Successfully withdraw')
                print('your account balance is : ',self.balance)
            else:
                print('insufficient balance')
        self.menu()


obj = MyAtm()