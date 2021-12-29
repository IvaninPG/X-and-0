





def print_field(fld):
    print(' Крестики нолики ')
    print(f'    0   1   2')
    print(f'  -------------')
    for i in range(3):
        row = ' | '.join(fld[i])
        print(f'{i} | {row} |')
        if i < 2:
            print(f'  -------------')
    print(f'  -------------')



def input_coords():
    while True:
        coords = input('Введите координаты через пробел x y: ').split()

        if len(coords) != 2:
            print('Введите обе координаты')
            continue

        _x, _y = coords

        if not(_x.isdigit()) or not(_y.isdigit()):
            print('Введите цифры')
            continue

        _x, _y = int(_x), int(_y)

        if 0 > _x or _x > 2 or 0 > _y or _y > 2:
            print('Координаты вне игрового поля')
            continue

        if field[_y][_x] != ' ':
            print('Данная клетка уже занятя')
            continue

        return _x, _y



def win_condition(_x, _y):
    player = field[_y][_x]

    if player == ' ':
        return False

    line = set(field[_y])
    if len(line) == 1 and player in line:
        return True
    line.clear()

    for i in range(3):
        line.add(field[i][_x])
    if len(line) == 1 and player in line:
        return True
    line.clear()

    if _x == _y or _x + _y == 2:
        for i in range(3):
            line.add(field[i][i])
        if len(line) == 1 and player in line:
            return True
        line.clear()
        for i in range(3):
            line.add(field[i][2-i])
        if len(line) == 1 and player in line:
            return True
    return False



field = [[' '] * 3 for i in range(3)]

counter = 9
turn = False

print_field(field)


while counter > 0:
    if not turn:
        print("Ход X")
    else:
        print("Ход O")

    x, y = input_coords()

    if not turn:
        field[y][x] = 'X'
    else:
        field[y][x] = 'O'

    print_field(field)

    if win_condition(x, y):
        print(f'Игрок {"O" if turn else "X"} выиграл!')
        break
    turn ^= True
    counter -= 1


if not counter:
    print('Ничья')
