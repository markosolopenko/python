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

    widths_of_all = []
    widths_of_col = []
    lin = ''
    for rows in table_data:
        for column in rows:
            length = len(str(column))
            lin += str(length)
        widths_of_all.append(lin)
        lin = ''
    for num in widths_of_all:
        widths_of_col.append(max(num))
    # for column in table_data:
    #     max_length = reduce(
    #         lambda x, y: max(x, y),
    #         map(
    #             lambda x: len(str(x)),
    #             column
    #         ))

        # widths_of_col.append(max_length)

    array = np.array(table_data).transpose()

    for row in array:
        row_str = ''
        for word, width in zip(row, widths_of_col):
            width = int(width)
            row_str += str(word).rjust(width + offset)
        print(row_str)


if __name__ == "__main__":

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob Dylan', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose'],
                 [Person("Mark","Henry"),Person("Robin","One"),Person("Mark","Henry"),Person("Robin","One")],
                 [1,2,3,4444]]

    print(table_printer(tableData))