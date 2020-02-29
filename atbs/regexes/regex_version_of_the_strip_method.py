import re
def re_strip(string, char="\s"):
    result = re.sub(f"^{char}+", "", string)
    result = re.sub(f"{char}+$", "", result)
    return result
print(re_strip("    Adasdv  "))