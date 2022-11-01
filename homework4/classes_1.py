from unicodedata import name


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


    def increase_speed(self, value):
        self.max_speed = self.max_speed + value


    def break_speed(self):
        self.max_speed = 0


    def mileage_info(self):
        print(self.mileage)   


class Bus(Vehicle):
    def seating_capacity(self):
        print('seating_capacity')
        

print(issubclass(Bus, Vehicle))   

school_bus = Bus(max_speed = 120, mileage = 50000)

print(isinstance(school_bus, Bus))
print(isinstance(school_bus, Vehicle))


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    
    def school_address(self):
        print('school_address')


    def main_subject(self):
        print('main_subject')


class SchoolBus(School, Bus):
    def bus_school_color(self):
        print('bus_school_color') 


class Bear:

    def eat(self):
        print('Bear eat')


class Wolf:

    def eat(self):
        print('Wolf eat')

Bear_1 = Bear()
Wolf_1 = Wolf()

for animal in (Bear_1, Wolf_1):
    animal.eat()



class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, *args, **kwargs):
        population = kwargs.get('population')
        if population < 1500:
            print("Your city is too small")
            return None
        return super().__new__(City)
    

    
city_1 = City('Lviv', population=100)
city_2 = City('Kyiv', population=2000)
print(city_1)
print(city_2)
