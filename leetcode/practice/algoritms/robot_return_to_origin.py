def robot_move(steps):
    x = {'L': 1, 'R': -1}
    y = {'U': 1, 'D': -1}
    move_x = 0
    move_y = 0
    for i in steps:
        if i in x:
            move_x += x[i]
        elif i in y:
            move_y += y[i]
    if move_x == 0 and move_y == 0:
        return True
    return False


if __name__ == '__main__':
    print(robot_move("LDRRLRUULR"))