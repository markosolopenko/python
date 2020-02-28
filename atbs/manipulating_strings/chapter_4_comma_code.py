def creating_the_comma_code(spam):
    resalt = ""
    for characters in spam:
        if spam.index(characters) == len(spam) - 1:
            resalt += "and " + characters + "."
        else:
            resalt += characters + ", "
    return resalt


# def creating_the_comma_code(spam):
#     return ', '.join([word for word in spam[:-1]]) + ' and ' + spam[-1]

print(creating_the_comma_code(['apples', 'bananas', 'tofu', 'cats']))
