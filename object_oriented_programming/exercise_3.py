class Box:
    def add(self):
        raise NotImplementedError

    def empty(self):
        raise NotImplementedError

    def count(self):
        raise NotImplementedError


class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.count2 = 0

    def box(self):
        return self.name, self.value


class ListBox(Item, Box):
    def __init__(self, name, value):
        self.list_of_items = []
        super().__init__(name, value)

    def empty(self):
        count = 0
        for char in self.box():
            self.list_of_items.append(char)
            count = self.count()
        print(f'Amount of items = {count}')
        return self.list_of_items

    def count(self):
        self.count2 += 1
        return self.count2

class DictBox(Item, Box):
    def __init__(self, name, value):
        self.dict_of_items = {}
        super().__init__(name, value)

    def empty(self):
        count = 0
        for k in self.box():
            self.dict_of_items[k] = 1
            count = self.count()
        print(f'Amount of key, values = {count}')
        return self.dict_of_items

    def count(self):
        self.count2 += 1
        return self.count2

a = DictBox('Marko', 12)
print(a.empty())