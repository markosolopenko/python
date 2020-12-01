import numpy as np

with open('input.txt', 'r') as file:
    instructions = file.read().splitlines()

array_np = np.zeros((6, 50))


def lights_bright():
    for line in instructions:
        if line.startswith('rect'):
            pos_x, pos_y = line.split()[1].split('x')
            array_np[:int(pos_y), :int(pos_x)] = 1
        elif line.startswith('rotate'):
            _, ax, pos, _, shift = line.split()
            pos = int(pos.split('=')[1])
            shift = int(shift)
            if ax == 'row':
                array_np[pos] = np.roll(array_np[pos], shift)
            elif ax == 'column':
                array_np[:, pos] = np.roll(array_np[:, pos], shift)

    print(f'If to look in my result there are {np.sum(array_np)} lights which brights')
    print('>>>>>>>>')
    for row in array_np:
        for line in row:
            if line == 1.0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    # print(f'After the swipe the card I am able to see this code {}')


if __name__ == "__main__":
    lights_bright()