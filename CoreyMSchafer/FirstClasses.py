from distutils.command.build_scripts import first_line_re
from re import L


class Employee:   # class
    def __init__(self, first, last, pay):
        self.first = first    # instance Variable
        self.last = last
        self.pay = pay
        self.email = first +'.'+ last + '@compayny.com'

    def fullname(self): # this self can be anything like "fullname(john):"
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Alex', 'Yaya', '5000') # object of the class Employee created with name emp1
emp2 = Employee('Bob', 'Xami', '8000') # unique instance of Employee class

print(emp1.first)
print(emp1.fullname())
print(Employee.fullname(emp2))
print(emp2.email)