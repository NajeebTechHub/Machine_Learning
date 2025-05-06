# Q-2: Bank Class
# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details. Give the complete code for the BankAccount class.

class BankAccount:

    def __init__(self,an,n,b):
        self.accountNumber = an
        self.name = n
        self.balance = b

    def deposit(self,balance):
        userAccountNumber = int(input('Enter account number : '))
        userName = input('Enter user name : ')
        self.user_balance = balance

        if userAccountNumber == self.accountNumber and userName == self.name:
            self.balance = self.balance + self.user_balance
            print('balance deposited successfully')
            print('your current balance is : ',self.balance)

    def withdrawal(self,balance):
        userAccountNumber = int(input('Enter your account number : '))
        userName = input('Enter user name : ')
        self.userBalance = balance
        if userAccountNumber == self.accountNumber and userName == self.name and self.userBalance <= self.balance:
            self.balance = self.balance - self.userBalance
            print('Withdraw successfull')
            print('your current balance is : ',self.balance)

    def display(self):
        print('Your account number is : ',self.accountNumber)
        print('Your user name is : ',self.name)
        print('Your account balance is : ',self.balance)

    def backFees(self):
        self.balance = self.balance * (5/100)
        print('After back fees your balance is : ',self.balance)




newAccount = BankAccount(1234, "najeeb" , 2800)

# newAccount.withdrawal(700)

# newAccount.deposit(1000)

newAccount.display()