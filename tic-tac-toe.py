
board = [' '] * 9

def draw_board():
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i], '|', board[1 + i], '|', board[2 + i], '|')
        print('-' * 13)

win_comb = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def check_winner():
    for combo in win_comb:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def check_draw():
    return ' ' not in board

def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        draw_board()
        position = int(input("Выберите позицию от 1 до 9: ")) - 1

        if board[position] == ' ':
            board[position] = current_player
            if check_winner():
                draw_board()
                print("Игрок", current_player, "победил!")
                game_over = True
            elif check_draw():
                draw_board()
                print("Ничья!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Недопустимый ход. Попробуйте еще раз.")

play_game()