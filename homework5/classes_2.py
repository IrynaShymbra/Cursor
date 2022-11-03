#1

import collections
import dataclasses


class Laptop:
    def __init__(self):
        battery_1 = Battery('GB_32')
        battery_2 = Battery('GB_64')
        battery_3 = Battery('GB_256')
        self.laptop = [battery_1.battery_capacity, battery_2.battery_capacity, battery_3.battery_capacity]

        
        
class Battery:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity        


dell = Laptop()
print (dell.laptop)

#2

class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string

        
        
class GuitarString:
    def __init__(self, string_type):
        self.string_type = string_type


nylon_string = GuitarString('nylon')       
cordoba = Guitar(nylon_string)

#3

class Calc:
    def __init__(self, num_1, num_2, num_3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

    def add_nums(self):
        return self.num_1 + self.num_2 + self.num_3


sum_of_num = Calc(1,2,3)
print(sum_of_num.add_nums())


#4

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
        
    @classmethod
    def carbonara(cls, forcemeat, tomatoes):
        return cls(forcemeat, tomatoes)


    @classmethod
    def bolognaise(cls, bacon, parmesan, eggs):
        return cls(bacon, parmesan, eggs)

pasta_1 = Pasta(["tomato", "cucumber"]) 
print(pasta_1.ingredients)

pasta_2 = Pasta(['bacon', 'parmesan', 'eggs'])
print(pasta_2.ingredients)


#5


#6

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

address_book =  AddressBookDataClass('S2345', 'Sergio Lakodini', '+367890231', 'Cordoba', 'sergiolako@gmail.com', '1993-02-15', 29)
print(address_book)     


#7

    
AddressBookDataClass = collections.namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
address_book = AddressBookDataClass('S2345', 'Sergio Lakodini', '+367890231', 'Cordoba', 'sergiolako@gmail.com', '1993-02-15', 29)
print(address_book[1][0])
