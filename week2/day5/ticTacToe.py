play_board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, " ", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", " ", 1],
    [1, " ", "-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-", " ", 1],
    [1, " ", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", " ", 1],
    [1, " ", "-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-", " ", 1],
    [1, " ", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", " ", 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def display_board(board):
    for row in board:
        for pixel in row:
            if pixel == 1:
                print("*", end=" ")
            else:
                print(pixel, end=" ")
        print('')


def check_value(players, value):
    for player in players:
        if value in player['positions']:
            return True
    return False


def player_input(player, players):
    x = 0
    y = 0
    while True:
        row = int(input("please, insert in which row you want to add your sign "))
        column = int(input("please, insert in which column you want to add your sign "))

        if row >= 1 and row <=3 and column >= 1 and column <= 3:
            if row == 1:
                x = 1
            elif row == 2:
                x = 3
            elif row == 3:
                x = 5

            if column == 1:
                y = 3
            elif column == 2:
                y = 7
            elif column == 3:
                y = 11

            if not is_contain(players, [x, y]):
                break
            else:
                print("the cell is taken")
        else:
            print("you added a wrong Row number, try again")


    player["positions"].append([x, y])
    return [x, y]


def change_the_board(sign, coordinades, board):
    board[coordinades[0]][coordinades[1]] = sign


def is_contain(values, search_for):
    for value in values:
        if search_for in value['positions']:
            return True
    return False


def check_win(board):
    for i in range(1, 6, 2):
        if board[i][3] == board[i][7] and board[i][7] == board[i][11] and board[i][11] != " ":
            print(f"player {board[i][3]} is a winner")
            return True

    for i in range(3, 12, 4):
        if board[1][i] == board[3][i] and board[3][i] == board[5][i] and board[5][i] != " ":
            print(f"player {board[1][i]} is a winner")
            return True

    if board[1][3] == board[3][7] and board[3][7] == board[5][11] and board[5][11] != " ":
        print(f"player {board[1][3]} is a winner")
        return True
    elif board[5][3] == board[3][7] and board[3][7] == board[1][11] and board[1][11] != " ":
        print(f"player {board[3][7]} is a winner")
        return False
    else:
        return False


def play(board):
    players = [
        {
            'sign': "X",
            'positions': []
        },
        {
            'sign': "O",
            'positions': []
        }
    ]

    print("hello it's a new game")
    i = 0
    end_point = 0
    while end_point < 9 and not check_win(board):
        if end_point < 9:
            if i == 0:
                display_board(board)
                coordinates = player_input(players[0], players)
                change_the_board(players[0]["sign"], coordinates, board)
                end_point += 1
                i = 1
            else:
                display_board(board)
                coordinates = player_input(players[1], players)
                change_the_board(players[1]["sign"], coordinates, board)
                end_point += 1
                i = 0
        else:
            print("end of game, no one wins!")


play(play_board)
