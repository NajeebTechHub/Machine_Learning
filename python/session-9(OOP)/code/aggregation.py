class person:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f'i am {self.name} my age is {self.age} i am from {self.address.get_destrict()},{self.address.tahsil},{self.address.postcode}')


    def edit_profile(self,new_name,new_destrict,new_tahsil,new_postcode):
        self.name = new_name
        self.address.edit_address(new_destrict,new_tahsil,new_postcode)


class address:

    def __init__(self,destrict,tahsil,postcode):
        self.__destrict = destrict
        self.tahsil = tahsil
        self.postcode = postcode

    def get_destrict(self):
        return self.__destrict
    
    def edit_address(self,new_destrict,new_tahsil,new_postcode):
        self.__destrict = new_destrict
        self.tahsil = new_tahsil
        self.postcode = new_postcode


add1 = address('mardan','katlang',23200)
per1 = person('Najeeb',23,add1)
per1.display()

per1.edit_profile('haseeb','mardan','katlang',23200)
per1.display()