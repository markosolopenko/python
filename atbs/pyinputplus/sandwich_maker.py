import pyinputplus as pyip

def make_sandwich():
    sum_of_sandwich = 0
    a = 1
    dif = ''
    count = 0
    amount_of_sandwiches = pyip.inputInt(prompt="How many sandwiches do you want? ", min=1)
    if amount_of_sandwiches == 1:
        print(f'Ok {amount_of_sandwiches} sandwich')
    print(f'Ok {amount_of_sandwiches} sandwiches')
    while amount_of_sandwiches != count:
        bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'])
        sum_of_sandwich += 2
        protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
        sum_of_sandwich += 4
        cheese_or_no = pyip.inputYesNo(prompt="Do you want cheese or not?")
        if cheese_or_no == 'no':
            sendwich = f'{bread_type} bread, {protein_type} protein and no cheese!! It cost is {sum_of_sandwich}$'
        else:
            cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
            sum_of_sandwich += 5
            sendwich = f'{bread_type} bread, {protein_type} protein and {cheese_type} cheese!!! It cost is {sum_of_sandwich}$'
        dif += f'{a} with: {sendwich} \n'
        sendwich = ''
        a += 1
        count += 1
        sum_of_sandwich = 0
    print(dif)
if __name__ == "__main__":
    make_sandwich()