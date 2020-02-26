def displayInventory(dict_inventory):
    new_string = ''
    sum_of_items = 0
    for k,v in dict_inventory.items():
        sum_of_items += v
        new_string += str(v) + " " + k + "\n"
    print("Inventory: ")
    print(new_string)
    print("Total number of items: " + str(sum_of_items))


displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})