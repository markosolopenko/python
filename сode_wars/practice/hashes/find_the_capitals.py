def capital(capitals):
    capital_of_place = ''
    result = []
    for a in capitals:
        if 'state' in a:
            capital_of_place = f'The capital of {a["state"]} is {a["capital"]}'
        elif 'country' in a:
            capital_of_place = f'The capital of {a["country"]} is {a["capital"]}'
        result.append(capital_of_place)
    return result




if __name__ == '__main__':
    print(capital([{'state': 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]))