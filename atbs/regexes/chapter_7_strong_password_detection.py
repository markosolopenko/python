import pyperclip, re

strong_pwd_regex = re.compile(r'\d+\s+')

password = strong_pwd_regex.search("12")
print(password.groups())
# matches = []
#
# for groups in strong_pwd_regex.findall(password):
#     if len(matches) < 8:
#         print('Password needs to be at least 8 characters long.')