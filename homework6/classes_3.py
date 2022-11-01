#1
from abc import ABC, abstractmethod


class FibonacciNumbers:
    curr_number = 1
    prev_number = 0
    counter = 0

    def __init__(self, max_count) -> None:
        self.max_count = max_count

    def __iter__(self):
        return self


    def __next__(self):
        if self.counter <= self.max_count:
            if self.counter <= 1:
                self.counter += 1    
                return self.counter - 1  
            self.curr_number += self.prev_number
            self.prev_number = self.curr_number - self.prev_number
            self.counter += 1
            return self.curr_number    
        raise StopIteration

for i in FibonacciNumbers(10):
    print(i)



#2
def fibo_numbers(max_count):
    curr_number = 1
    prev_number = 0
    counter = 0 
    while counter <= max_count:
        if counter <= 1:
            counter += 1
            yield counter - 1
        else:
            curr_number += prev_number
            prev_number = curr_number - prev_number
            counter += 1
            yield curr_number 
                
           
gen = fibo_numbers(10)
for elem in gen:
    print(elem)



#3

gen_expr = (a ** 2 for a in range(11))
for elem in gen_expr:
    print(elem)


#4

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        print('Hallo')

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):

    def screen(self):
        print('Hallo')

    def keyboard(self):
        print ('Hi')  

    def touchpad(self):
        print('Touch')

    def webcam(self):
         print('Take a look')           

    def ports(self):
        print('Ports')

    def dynamics(self):
        print('Speak')


#5

class Car(ABC):
        
    def drive(self):
        print('I am driving')


    def stop(self):
        print('I am stopping')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError

