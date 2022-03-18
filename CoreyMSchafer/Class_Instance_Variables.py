
class Employee:

    num_of_emps = 0 # class variable
    grow_by = 1.05

    def __init__(self, first, last, pay):
        self.first = first   # instance variable
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.grow_by)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps)
print(emp_1.pay)

emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)

print(Employee.grow_by)
print(emp_1.grow_by)
print(emp_2.grow_by)

emp_1.grow_by = 1.10
print(emp_1.__dict__)

print(emp_1.grow_by)

print(Employee.__dict__)
