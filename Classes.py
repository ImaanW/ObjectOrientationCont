# Python object - Orientation Programming
# creating the class
class Employee:

    raise_amount = 1.04
    # in the brackets are parameters,
    # init(constructor) method initialised class attributes and takes self has instance and the others arguments a sobjects
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
# above shows instance varibles that are set using the self arguement
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#INHERETENCE
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
                self.employees = []
        else:
                self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())


# SPECIAL METHODS
# __str__(self): return a python readable representation
# __repr__(self): return a python readable representation - change how our objects are displayed
# __innit__ initialise an object

# OPERATOR OVERLOAD SPECIAL METHODS
# __add__ +
# __sub__ -
# __eq__ ==
# __ge__ >=
# __lt__ <
# __invert__
# __getitem__(self,key) container element evaluation
# __setitem__(self,key) container element assignment

# below are objects of the class Employee
emp_1 = Employee('imaan','williams', 50000)
emp_2 = Employee('test', 'user', 800,)
# here shows when we estanciated our developers, it first looked in our developer
#class for init method, didnt find so inheritered from Employee class
#which is why its also printer the same when Employee was estanciated
#it searched for enstanciation through the mthro resoltuion order(going up through code)

#using the print(help())will show

# print(emp_1,emp_2)
dev_1 = Developer('theo','maloney',100000,'java')
dev_2 = Developer('dionne','williams', 300000,'java script')
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

mgr_1 = Manager('sue','smith',100,[dev_1])
print(mgr_1.email)
mgr_1.print_emps()

print(isinstance(mgr_1,Manager))
# Returns true as mgr_1, is an instance of Manager and Employee
print(issubclass(Developer,Employee))
# Returns tues as developer is a subclass of Manager


# encapsulation
# _ or __ private attributes

# polymorphisms
#Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.