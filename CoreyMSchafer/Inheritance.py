class Employee:
    
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
#       Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())

dev1 = Developer("John", "Babbar", 7000, 'Python')
dev2 = Developer("Dany", "Mamu", 8000, 'Java')


mgr1 = Manager('sue', 'smith', 9000, [dev1])

# print(isinstance(mgr1, Manager))
# print(isinstance(mgr1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Developer))


# print(mgr1.email)

# print(mgr1.print_emps())

# mgr1.add_emp(dev2)
# print(mgr1.print_emps())

# mgr1.remove_emp(dev1)
# print(mgr1.print_emps())

# print(dev1.email)
# print(dev1.prog_lang)
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
