"""
We should to find the shortest word in the string
"""
def find_short(s):
    b = []
    # Making all character lower
    s = s.lower()
    for a in s.split():
        c = len(a)
        b.append(c)
    return min(b)
print(find_short("bitcoin take over the world maybe who knows perhaps"))