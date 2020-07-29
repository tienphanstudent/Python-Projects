import datetime

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
        Employee.num_of_employees += 1

    def __repr__(self):
        return "Employee(\"{first}\", \"{last}\", \"{pay}\")".format(first=self.first, last=self.last, pay=self.pay)

    def __str__(self):
        return "{fullname} - {email}".format(fullname=self.fullname(), email=self.email)

    def fullname(self):
        return "{first}{last}".format(first=self.first, last=self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, name, last, pay, prog_lang):
        super().__init__(name, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, name, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print(self):
        for emp in self.employees:
            print("-->", emp.fullname())

employee1 = Employee("nigger", "domus", 1)
employee2 = Employee("haha", "such a memer", 2)

# my_date = datetime.date(2020, 7, 27)
#
# print(Employee.is_workday(my_date))
#
# print(employee1.fullname())

print(employee1)