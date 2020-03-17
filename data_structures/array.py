
class NoSpaceInArrayException(Exception):
    def __init__(self):
        super().__init__()


class CellIsOccupiedException(Exception):
    def __init__(self):
        super().__init__()


class Array:

    def __init__(self, size, default_value=None):
        self.size = size
        self.default_value = default_value
        self.data = []
        for i in range(size):
            self.data.append(default_value)

    def length(self):
        """
        Get array length
        :return:
        """
        return sum([1 for element in self.data
             if element is not self.default_value])

    def add(self, element):
        """
        Try to add new character to list
        :param element:
        :return:
        """
        if self.length() >= self.size:
            raise NoSpaceInArrayException()
        else:
            for index, el in enumerate(self.data):
                if el is self.default_value:
                    self.data[index] = element
                    break

    def insert(self, index, element, force=True):
        """
        Try to insert element at index
        :param index:
        :param element:
        :param force:
        :return:
        """
        if index < self.size:
            if self.data[index] is None:
                self.data[index] = element
            else:
                if force:
                    self.data[index] = element
                else:
                    raise CellIsOccupiedException()
        else:
            raise IndexError()

    def get(self, index):
        """
        Get the element by it index
        :param self:
        :param index:
        :return:
        """
        return self.data[index]

    def find(self, element):
        """
        find index of the first entry of the element in array
        :param self:
        :param element:
        :return:
        """
        for index, el in enumerate(self.data):
            if el == element:
                return index
        return None

    def find_all(self, element):
        """
        Get indices of all entries of the given element in array
        :param self:
        :param element:
        :return:
        """
        indices = []
        for index, el in enumerate(self.data):
            if el == element:
                indices.append(index)
        return indices

    def delete(self, element):
        """
        Delete certain element
        :param self:
        :param element:
        :return:
        """
        index = self.find(element)

        if index is not None:
            for i in range(index, self.size - 1):
                self.data[i] = self.data[i+1]
            self.data[-1] = self.default_value

    def delete_all(self, element):
        while self.find(element) is not None:
            self.delete(element)

    @classmethod
    def from_seq(cls, sequence):
        seq_length = len(sequence)
        arr = cls(seq_length)
        for el in sequence:
            arr.add(el)
        return arr

    def __str__(self):
        """
        Representation array
        :param self:
        :return:
        """
        return '[' + ', '.join([str(x) for x in self.data]) + ']'

    def __add__(self, other):
        """
        Method to add two arrays
        :param self:
        :param other:
        :return:
        """
        return self.from_seq(self.data + other.data)


if __name__ == "__main__":

    my_array = Array(5)

    assert my_array.data == [None, None, None, None, None]

    my_array.add('M')
    my_array.add('A')

    assert my_array.data == ['M', 'A', None, None, None]

    my_array.delete('M')

    assert my_array.data == ['A', None, None, None, None]

    assert my_array.length() == 1

    my_array.insert(index=3, element='O', force=True)

    assert my_array.data == ['A', None, None, 'O', None]
    print(my_array)

    # my_array.insert(index=5, element='S', force=True)

    # my_array.insert(index=3, element='P', force=False)

    #my_array.add('S')

    #assert my_array.data == ['A', 'S', None, 'O', None]

    # my_array.add('S')
    # my_array.add(5)

    #assert my_array.data == ['A', 'S', 'S', 'O', 5]

    # my_array.add('9')

    # my_array.delete_all('S')

    # assert my_array.data == ['A', 'O', 5, None, None]

    # assert my_array.find(5) == 4
    #
    # assert my_array.find_all('S') == [1, 2]
    #
    # second_array = Array(3)
    #
    # second_array.add('B')
    # second_array.add('C')
    #
    # print(my_array)
    # print(second_array)
    # print(my_array + second_array)
    #
    # arr = Array.from_seq((1, 2, 32, 13, 21, 32))
    #
    # print(arr)