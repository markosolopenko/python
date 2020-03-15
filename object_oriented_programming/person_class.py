import datetime

class Person:

    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.days = 0

        self.years_old = 0


    def calculate(self):
        today = datetime.date.today()
        self.years_old = today.year - self.birth_date.year
        if today < datetime.date(today.year, self.birth_date.month, self.birth_date.day):
            self.years_old -= 1
        if self.days > 0:
            return f'{self.name} is {self.years_old} years old. {self.days} days.'
        else:
            return f'{self.name} is {self.years_old} years old'


    def convert_to_days(self):
        self.days = 365 * self.years_old

    def reload(self):
        self.days += 1

person = Person('Mark', 'Kokos', datetime.date(1997,10,16))

print(person.calculate())
person.convert_to_days()
person.reload()
print(person.calculate())
person.reload()
print(person.calculate())
person.reload()
print(person.calculate())





