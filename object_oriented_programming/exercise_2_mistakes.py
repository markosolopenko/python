class UserExistingError(Exception):
    pass

class AgeLessError(Exception):
    pass

class AgeNotReal(Exception):
    pass

class InvalidEmail(Exception):
    pass

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


data_list = [("Kora", "some@gmail.com", 25),
             ("Kira", "kilos@gmail.com", 122),
             ("Alisa", "borza@gmail.com", 41)]

new_dict = {}
list_new = ''

for name, email, age in data_list:
    try:
        if age <= 16 and age > 0:
            raise AgeLessError
        elif age < 0:
            raise AgeNotReal
        elif name in new_dict:
            raise UserExistingError
        elif '@' not in email:
            raise InvalidEmail
    except AgeLessError:
        print(f'{name} is too yang')
    except AgeNotReal:
        print(f'age can\'t be less than zero!!!')
    except UserExistingError:
        print(f'This username {name} already exist')
    except InvalidEmail:
        print(f'Email address should has "@" symbol')
    else:
        new_dict[name] = email
for k, v in new_dict.items():
    print(f'{k}: {v}')


