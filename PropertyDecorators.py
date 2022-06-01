class Employee:

    raise_amount = 1.04
    # in the brackets are parameters,
    # init(constructor) method initialised class attributes and takes self has instance and the others arguments a subjects

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
# above shows instance varibles that are set using the self arguement
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
# SETTER
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
# DELETER
    @fullname.deleter
    def fullname(self,):
        print("delete name")
        self.first = None
        self.last = None


# Properties and decorators
# decorator prefixed with @
# @property decorator allows us to define a method and access it like an attribute
# no need for () when trying to access it if property decorator is used before
emp_1 = Employee('imaan','williams', 50000)
emp_2 = Employee('test', 'user', 800,)

# here setting new name, changing first name and last name
emp_1.fullname = ('Hamazah Williams')
print(emp_1.fullname)
print()

# the deleter
del emp_1.fullname