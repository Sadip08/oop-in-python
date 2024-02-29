class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Sadip','Tamang',1000)
emp2 = Employee('Madan','Tamang',5000)

print(emp1.fullname())
print(Employee.fullname(emp2))