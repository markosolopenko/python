def addToInventory(inv, dragon_loot):
    resalt = ''
    for invet in dragon_loot:
        if invet in inv.keys():
            inv[invet] += 1
        inv.setdefault(invet,1)
    for k,v in inv.items():
        resalt += str(v) + " " + k + "\n"
    print("Inventory: ")
    print(resalt)
print(addToInventory({'gold coin': 42,'rope': 1},['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']))

# print("{}{}".format(10, "10"))