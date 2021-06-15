import sys

print(sys.executable)
print(sys.version)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        # print(f'Created Employee: {self.fullname}, Email: {self.email}')

    def __repr__(self):
        return f"Created Employee: {self.fullname}"

    @property
    def email(self):
        # return '{}.{}@email.com'.format(self.first, self.last)
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        # return '{} {}'.format(self.first, self.last)
        return f"{self.first} {self.last}"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("James", "Web")
print(emp_1)
print(emp_2)
print(emp_1.first)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname)
print(emp_2.fullname)
