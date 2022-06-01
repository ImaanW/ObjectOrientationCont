class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return (f"my name is {self.first}, and my last name is {self.last}")
# built in method

class Employee(Person):
    def __init__(self, first, last, age, wage):
        super().__init__(first, last, age)
        self.wage = wage


class Customer:
    def __init__(self, first, last, order_no):
        self.first = first
        self.last = last
        self.order_no = order_no

    def info(self):
        return f"my name is {self.first}, and my last name is {self.last}"

# script instantiating based on Person class
p_1 = Person('imaan','williams',1)
p_2 = Person('jack','smith', 2)

emp_1 = Employee("elle","donald",23,1880)

# access the class attributes
print(p_1.first)
print(emp_1.wage)

# instantiating based on Customer class
customer1 = Customer('Jade',"Rowe", 2344)

print(customer1.first)
# Polymorphism example
print(customer1.info())
print(emp_1)
print(p_1)
