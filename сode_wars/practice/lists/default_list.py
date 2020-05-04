class DefaultList:
    def __init__(self, list_elements, default_value):
        self.list_elements = list_elements
        self.default_value = default_value

    def __getitem__(self, index):
        if index >= len(self.list_elements) or index < -len(self.list_elements):
            return self.default_value
        return self.list_elements[index]

    def __setitem__(self, index, value):
        self.list_elements[index] = value

    def extend(self, list_a):
        self.list_elements.extend(list_a)

    def append(self, element):
        self.list_elements.append(element)

    def remove(self, element):
        self.list_elements.remove(element)

    def insert(self, index, element):
        self.list_elements.insert(index, element)

    def pop(self, index):
        self.list_elements.pop(index)
    def __str__(self):
        return self.list_elements

lst = DefaultList([9131, 'BC u', True, 4178, 8853, True, 3208, 1307, True], 5579)
lst.extend([12,32,44,"BCD"])
print(lst[100000000000000])

