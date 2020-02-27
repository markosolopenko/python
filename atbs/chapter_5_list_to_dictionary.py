
from atbs.chapter_5_fantasy_game_invenory import displayInventoryShort


def addToInventory(inv, dragon_loot):
    for item in dragon_loot:
        if item in inv:
            inv[item] += 1
        inv.setdefault(item, 1)
        # item[item] = 1

    displayInventoryShort(inv)

    # for k, v in inv.items():
    #     result += str(v) + " " + k + "\n"
    # print("Inventory: ")
    # print(result)


addToInventory({'gold coin': 42, 'rope': 1},['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])

# print("{}{}".format(10, "10"))


# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# print(my_dict)
#
# my_dict.setdefault('d', 4)
#
