"""
We should to find the length of the shortest word in the string
"""

def find_short(s):
    b = []
    # Making all character lower
    s = s.lower()
    for a in s.split():
        c = len(a)
        b.append(c)
    return min(b)


def find_short(s):
    # list comprehension solution
    return min([len(x) for x in s.split(' ')])

print(find_short("bitcoin take over the world maybe who knows perhaps"))
