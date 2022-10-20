import numbers


int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

def define_ids():
    """Define ids for all global variables"""
    print(id(int_a))
    print(id(str_b))
    print(id(set_c))
    print(id(lst_d))
    print(id(dict_e))


def add_numbers():
    """Add numbers to the list"""
    print(id(lst_d))
    lst_d.extend([4,5])
    print(id(lst_d))


def define_types():
    """Define the type for each object of all global variables """
    print(type(int_a))
    print(type(str_b))
    print(type(set_c))
    print(type(lst_d))
    print(type(dict_e))     


def check_types():
    """Check the type of the objectes for all global variables """
    print(isinstance(int_a,int))
    print(isinstance(str_b,str))
    print(isinstance(set_c,set))
    print(isinstance(lst_d,list))
    print(isinstance(dict_e,dict))


def replace_placeholders():
    apples = 3
    peaches = 5
    print("Anna has {} apples and {} peaches.".format(apples,peaches))
    print("Anna has {1} apples and {0} peaches.".format(5,3))
    print("Anna has {apples} apples and {peaches} peaches.".format(apples=3, peaches=5))
    print("Anna has {:5s} apples and {:3s} peaches.".format(apples, peaches))
    print(f"Anna has {apples} apples and {peaches} peaches.")
    print(f"Sum of {apples} and {peaches} is {apples + peaches}")
    print("Anna has %d apples and %d peaches." % (apples, peaches))
    print("Anna has %(apples)s apples and %(peaches)s peaches." % {"apples":apples, "peaches":peaches})

"""
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)

"""

def convert_regular_to_comprehension():
    lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
    print(lst)


"""list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]"""

def convert_comprehension_to_regular():
    lst = []
    for num in range(10):
        if num % 2 == 0:
            lst.append(num // 2)
        else:
            lst.append(num * 10)   
    print(lst) 


"""d = {}
   for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
"""  
"""d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
"""

def convert_regular_to_dict_comprehension():
    d = {num:num **2 for num in range(1, 11)if num % 2 == 1}
    print(d)
    d = {num **2 if num % 2==1 else num // 0.5 for num in range (1,11)}
    print(d)


"""dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}"""
"""dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}"""

def convert_dict_comprehension_to_regular():
    d = {}
    for num in range(10):
        if num **3 % 4 == 0:
            d[num] = num **3

    d = {}
    for num in range(10):
        if num **3 % 4 == 0:
            d[num] = num **3
        else:
            d[num] = num    


"""def foo(x, y):
    if x < y:
        return x
    else:
        return y
"""                
foo = lambda x, y: x if x < y else y


"""foo = lambda x, y, z: z if y < x and x > z else y"""

def foo(x,y,z):
    if y < x and x > z: 
        return z    
    else:
        return y


"""lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]"""

lst = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst))

lst1 = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst1, reverse=True))

lst2 = [5, 18, 1, 24, 33, 15, 13, 55]
def multiply_to(num):
    return num * 2

lst3 = list(map(multiply_to,lst2))
print(lst3)

lst4 = list(map(lambda num: num * 2, lst2))
print(lst4)


list_A = [2, 3, 4]
list_B = [5, 6, 7]

def corresponding(numbers):
    index, item = numbers
    return item ** list_B[index]

lst5 = list(map(corresponding, enumerate(list_A))) 
print(lst5)

lst_6 = [5, 18, 1, 24, 33, 15, 13, 55]

filtered_lst = list(filter(lambda num:num % 2 == 1, lst_6))
print(filtered_lst)

lst_7 = list(filter(lambda num:num < 0, range(-10, 10)))
print(lst_7)


list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

lst_8 = list(filter(lambda item: item in list_2, list_1))
print(lst_8)
