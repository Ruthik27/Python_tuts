
from xml.dom.minicompat import EmptyNodeList


class Employee:
    
    num_emps = 0
    raise_by = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+ last + '@company.com'
    
        Employee.num_emps += 1

    def grow(self):
        self.pay = int(self.pay * self.raise_by)

    def fullname(self):
        return '{} {}' .format(self.first, self.last)

    @classmethod
    def set_raise(cls, amt):
        cls.raise_by = amt
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('_')
        return cls(first, last, pay)

    @staticmethod # dont operate on instance or class 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2000,7,27)
print(Employee.is_workday(my_date))

Employee.set_raise(1.50)
print(Employee.raise_by)

emp1 = Employee("jack", "beny", 5000 )
emp9 = Employee("popy", "star", 6000 )

emp_str_1 = 'alex_baba_4000'
emp_str_2 = 'jagu_damru_8000'
emp_str_3 = 'gangu_godse_6000'

emp2 = Employee.from_string(emp_str_1)
emp3 = Employee.from_string(emp_str_2)
emp4 = Employee.from_string(emp_str_3)

print(emp2.email)

Employee.grow(emp1)

print(emp1.pay)
print(emp1.email)

Employee.set_raise(1.2)
print(Employee.raise_by)
print(Employee.fullname(emp1))


print(Employee.num_emps)