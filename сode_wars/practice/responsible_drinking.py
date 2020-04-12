def hydrate(drink_string):
    glasses = 0
    for i in drink_string:
        if i.isdigit():
            glasses += int(i)
    if glasses > 1:
        return f'{glasses} glasses of water'
    return f'{glasses} glass of water'


if __name__ == '__main__':
    print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))