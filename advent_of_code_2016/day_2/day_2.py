from pprint import pprint

with open('day2.txt', 'r') as file:
    moves = file.read().split('\n')


def puzzle1():
    keypad = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    le = [0, 3, 6]
    ri = [2, 5, 8]
    password = ''
    curr = 5
    for line in moves:
        for letter in line:
            if letter == 'U':
                if curr - 3 in keypad:
                    curr = curr - 3
            elif letter == 'D':
                if curr + 3 in keypad:
                    curr = curr + 3
            elif letter == 'L':
                if curr - 1 in keypad and keypad.index(curr) not in le:
                    curr = curr - 1
            elif letter == 'R':
                if curr + 1 in keypad and keypad.index(curr) not in ri:
                    curr = curr + 1
        password += str(curr)

    print(password)


def puzzle2():
    with open('day2.txt', 'r') as infile:
        puzzle = infile.readlines()

    DIRECTIONS = {
        'R': 1,
        'L': -1,
        'D': 1j,
        'U': -1j,
    }

    KEYPAD_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    KEYPAD_2 = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, 'A', 'B', 'C', 0],
        [0, 0, 'D', 0, 0]
    ]

    def find_solutions(second_part=False):
        def is_inside(pos):
            if not second_part:
                return all(abs(coord) <= 1 for coord in {pos.real, pos.imag})
            else:
                return abs(pos.real) + abs(pos.imag) <= 2

        def get_key(pos):
            return str(keypad[int(pos.imag)][int(pos.real)])

        if not second_part:
            keypad = KEYPAD_1
            offset = 1 + 1j  # the center of the keypad
            pos = 0 + 0j  # start from the 5, in the center
        else:
            keypad = KEYPAD_2
            offset = 2 + 2j  # the center of the keypad
            pos = -2 + 0j  # start from the 5, two left from the center

        key_positions = []
        for line in puzzle:
            for direction in line.strip():
                new = pos + DIRECTIONS[direction]
                pos = new if is_inside(new) else pos
            key_positions.append(pos)

        return ''.join(get_key(pos + offset) for pos in key_positions)

    print("Ok, I've memorized the bathroom code:", find_solutions())
    print('....')
    print("Hmmm, this well-designed keypad is not the one I was expecting.")
    print("But let me try to open it with the same instuctions as before.")
    print("Here's the new code:", find_solutions(second_part=True))


if __name__ == '__main__':
    # puzzle1()
    puzzle2()