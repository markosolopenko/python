import re
import json

# def sum_of_all_numbers():
#     file = open('day12.txt').read()
#     all_numbers = re.findall('\-?[0-9]+', file)
#     result = 0
#     for i in all_numbers:
#         result += int(i)
#     print(result)


def hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj


def get_non_red_numbers(content):
    elements = str(json.loads(content, object_hook=hook))
    return map(int, re.findall(r"[-\d]+", elements))


if __name__ == "__main__":
    print(sum(get_non_red_numbers(open('day12.txt').readline())))