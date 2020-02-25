
import numpy as np


def pictures():

    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

    # picture = ''
      # for x in range(len(grid[0])):
    #     # print(x)
    #     for y in range(len(grid)):
    #         picture += grid[y][x]
    #     print(picture)
    #     picture = ''
    # print()  #
    # for x in range(len(grid[0])):
    #     # print(x)
    #     for y in range(len(grid)):
    #         picture += grid[y][x]
    #     print(picture)
    #     picture = ''
    # print()

    arr = np.array(grid)
    arr = arr.transpose()

    # print(arr)

    return '\n'.join([' '.join([y for y in x]) for x in arr])


if __name__ == "__main__":
    print(pictures())