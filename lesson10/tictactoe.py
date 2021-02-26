def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def validation(move, board):
    try:
        move = int(move)
    except:
        return False

    if move not in board:
        return False
    return True


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return True, board[each[0]]
    return False, None


def main():
    board = list(range(1, 10))
    player = 'X'

    while True:
        draw_board(board)
        move = input(f"Make your move for '{player}': ")
        valid = validation(move, board)
        if valid:
            move = int(move)
            board[move-1] = player
            is_win, user = check_win(board)
            if is_win:
                draw_board(board)
                print(f'Congratulation the player {user} is winner!')
                break
            elif all(isinstance(i, str) for i in board):
                draw_board(board)
                print('There is no winner! The game has ended as Draw!')
                break

            player = 'O' if player == 'X' else 'X'
            continue
        else:
            print('Make a right move')
            continue


# if __name__ == '__main__':
main()
