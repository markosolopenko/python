class Users:

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        self.new_dict = {}

    def __str__(self):
        return f'{self.username}, {self.email}, {self.age}'

    # def raise_errors(self):
    #     return [(self.age >= 16),
    #             (self.age > 0),
    #             (self.username not in self.new_dict),
    #             ('@' in self.email)]

    def loop(self):
        if self.age <= 16 and self.age > 0:
            return f'{self.username} is too yang'
        elif self.age < 0:
            return f'age can\'t be less than zero!!!'
        elif self.username in some:
            return f'This username {self.username} already exist'
        elif '@' not in self.email:
            return f'Email address should has "@" symbol'
        else:
            self.new_dict[self.username] =  self.email
            return self.new_dict
class Programmer(Users):
    def __init__(self, username, email, age):
        super().__init__(username, email, age)




class Accountant(Users):
    def __init__(self, username, email, age):
        super().__init__(username, email, age)


clas1 = Users("Kipper", "solejf@gmail.com", 22)
clas2 = Programmer("Kipper", "kolobok@gmail.com", 21)
clas3 = Accountant("Kas", "krakus@gmail.com", 41)

some = {}
for k in list((clas1,clas2,clas3)):
    some = k.loop()
    print(some)