import datetime # we will use this for date objects

# from datetime import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

        self.age = self._age()

        self.last_calculated_age = datetime.datetime.now()

        # self.age = self.age()

    def _age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    def age(self):
        if datetime.datetime.now() - self.last_calculated_age > \
                datetime.timedelta(days=365):
            return self._age()
        else:
            return self.age

    def lalala(self):
        pass

    # @property
    # def age(self):
    #     return self._age()
    #
    # @age.setter
    # def age(self, value):
    #     self._age = value


def print_all_attributes(obj):
    for x in dir(obj):
        if hasattr(obj, x):
            print(f'{x}: {getattr(obj, x)}')


def print_all_using_dict(obj):
    for k, v in obj.__dict__.items():
        print(f'{k}: {v}')


if __name__ == "__main__":
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),  # year, month, day
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )
    print('\n'.join([f'{key}: {value}' for key, value in Person.__dict__.items()]))
