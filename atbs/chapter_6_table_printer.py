import numpy as np

from functools import reduce

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'
class Motorola:

    def __init__(self, model, cost):
        self.model = model
        self.cost = cost

    def __str__(self):
        return f'{self.model} {self.cost}'



def table_printer(table_data, offset = 2):

    widths_of_col = []

    for column in table_data:
        max_length = reduce(
            lambda x, y: max(x, y),
            map(
                lambda x: len(str(x)),
                column
            ))

        widths_of_col.append(max_length)

    array = np.array(table_data).transpose()

    for row in array:
        row_str = ''
        for word, width in zip(row, widths_of_col):
            row_str += str(word).rjust(width + offset)
        print(row_str)


if __name__ == "__main__":

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob Dylan', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose'],
                 [1, 2, 3, 4444],
                 [Person('Bob', 'Dylan'), Person('Izzy', 'Pop'), Person('Madonna', 'Lalla'), Person('A', 'Bo')]]

    table_printer(tableData)