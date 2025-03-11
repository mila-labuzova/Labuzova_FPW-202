# приветствие и правила ввода
def welcome():
    print('''Добро пожаловать в игру "Крестики-нолики"
Формат ввода: xy
    x - номер строки
    y - номер столбца
Пожалуйста, используйте только две цифры в диапазонах от 0 до 2''')
    print()
# создаем поле игры
field = [[' '] * 3 for i in range(3)]
# вывод текущего состояния поля
def show_field():
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i in range(3):
        print(f'{i} |',' | '.join(field[i]),'|')
        print('---------------')
# получение координат от пользователя
def user_input():
    while True:
        coord = input('Введите координаты: ')
        if len(coord) != 2:
            print('Неверное количество символов. Введите 2 координаты!')
            continue
        if not (coord.isnumeric()):
            print('Недопустимые символы. Используйте только цифры!')
            continue
        x, y = map(int, coord)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Выход за пределы поля. Введите новые координаты.')
            continue
        if field[x][y] != ' ':
            print('Клетка занята. Введите новые координаты.')
            continue
        return x, y
# проверка выигрыша
def win_game():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coord in win_coord:
        lst = []
        for i in coord:
            lst.append(field[i[0]][i[1]])
            if lst == ['X', 'X', 'X']:
                print('Крестик выиграл!')
                return True
            if lst == ['0', '0', '0']:
                print('Нолик выиграл!')
                return True
# начинаем игру
welcome()
show_field()
count = 0
while True:
    count += 1
    if count % 2 == 1:
        print('Крестик ходит!')
    else:
        print('Нолик ходит!')
    x, y = user_input()
    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    (show_field())
    if win_game():
        break
    if count == 9:
        print('Ничья!')
        break