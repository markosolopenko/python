import numpy as np
def table_printer():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    wight_of_col = []
    colWight = [0] * len(tableData)
    print(colWight)
    # arr = np.array(tableData)
    # arr = arr.transpose()
    #
    # return '\n'.join([' '.join([y for y in x]) for x in arr])
if __name__ == "__main__":
    print(table_printer())