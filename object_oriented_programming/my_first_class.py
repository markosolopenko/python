class Array():
    def __init__(self, size, default_value):
        self.size = size
        self.arbitrary_array = []
        self.default_value = default_value
    ## Get the amount of characters
    def length(self):
        count_characters_in_array = 0
        for char in self.arbitrary_array:
            count_characters_in_array += 1
        print(f'The amount of characters are: {count_characters_in_array}')
    # Try to add new character to list
    def add(self,element):
        if len(self.arbitrary_array) == self.size:
            print("Sorry but array is full!!!")
        else:
            self.arbitrary_array.append(element)
            print(f'This element {element} attached to list -> {self.arbitrary_array}')
    # Try to insert element at index
    def insert(self,index,element,force=True):
            if force == True:
                self.arbitrary_array.insert(index,element)
                print(self.arbitrary_array)
            else:
                print(f'Oops element with this index {index} already exist {self.arbitrary_array}')
    # Get the element by it index
    def get(self,index):
        print(f'The element with this index if {self.arbitrary_array[index]}')
    # find index of the first entry of the element in array
    def find(self,element):
        print(f'First element has index {self.arbitrary_array.index(element)}')
    # Get indices of all entries of the given element in array
    def find_all(self,element):
        all_indexes_of_element = []
        for index, characters in enumerate(self.arbitrary_array):
            if characters == element:
                all_indexes_of_element.append(index)
        if all_indexes_of_element:
            print(f'This element {element} occures on this positions in list {all_indexes_of_element}')
        else:
            print(f'This element "{element}" not in array')
    # Delete certain element
    def delete(self, element):
        self.arbitrary_array.remove(element)
    # Representation array
    def __str__(self):
        print(self.arbitrary_array)
    # Method to add two arrays
    def __add__(self, other):
        print(other + self.arbitrary_array)
a = Array(5,4)


