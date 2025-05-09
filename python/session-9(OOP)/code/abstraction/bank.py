from abc import ABC,abstractmethod

class BankApp(ABC):

    def database(self):
        print('database connected')

    @abstractmethod
    def security(self):
        pass


class mobileApp(BankApp):

    def login(self):
        print('login')

    # must be write because it is abstract method
    def security(self):
        print('security')

m = mobileApp()
print(m.security())