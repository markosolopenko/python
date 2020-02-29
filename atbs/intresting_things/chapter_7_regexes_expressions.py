import re
"""
Finding Patterns of Text Without Regular Expressions
"""
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#   chunk = message[i:i+12]
#   print(chunk)
# print('Done')


#Finding Patterns of Text with Regular Expressions
# regexes - (\d{3}-\d{3}-\d{4})
# Creating Regex Objects
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Matching Regex Objects
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())
# # Grouping with Parentheses
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo.group(1)
# '415'
# mo.group(2)
# '555-4242'
# mo.group(0)
# '415-555-4242'
# mo.group()
# '415-555-4242'
# mo.groups()
# ('415', '555-4242')
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# mo.group()
# 'Batmobile'
# mo.group(1)
# 'mobile'

# Findall Method
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']
import re
# def create_phone_number(n):
#     return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
#
