import re
def password_detection():
    while True:
        user_password = input("Enter your password: ")
        s = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',user_password)
        if s:
            print('Good password!!!')
            break
        else:
            print("You password is not strong!!!")
            print("Try again")

if __name__ == "__main__":
    password_detection()