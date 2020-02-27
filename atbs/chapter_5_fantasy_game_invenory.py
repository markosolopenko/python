
def displayInventory(item_to_count: dict):
    inventory_list = ''
    sum_of_items = 0
    for k, v in item_to_count.items():
        sum_of_items += v
        # new_string += str(v) + " " + k + "\n"
        inventory_list += f'{v} {k}\n'
    print(f"Inventory:")
    print(inventory_list)
    print(f"Total number of items: {sum_of_items}")


def displayInventoryShort(item_to_count: dict):

    print(f'Inventory:')
    for k, v in item_to_count.items():
        print(f'{v} {k}')
    print(f'Total number of items: {sum([v for k, v in item_to_count.items()])}')


if __name__ == "__main__":
    displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})
    displayInventoryShort({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})