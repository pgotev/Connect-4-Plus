def check_win_condition(r, c):
    player = field[r][c]

    def check_horizontal():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= c + i < cols:
                if field[r][c + i] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= c - i < cols:
                if field[r][c - i] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    def check_vertical():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= r + i < rows:
                if field[r + i][c] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= r - i < rows:
                if field[r - i][c] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    def check_diagonal():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= r + i < rows and 0 <= c + i < cols:
                if field[r + i][c + i] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= r - i < rows and 0 <= c - i < cols:
                if field[r - i][c - i] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    def check_reverse_diagonal():
        sequence_counter = 1
        for i in range(1, win_condition):
            if 0 <= r + i < rows and 0 <= c - i < cols:
                if field[r + i][c - i] == player:
                    sequence_counter += 1
                else:
                    break
        for i in range(1, win_condition):
            if 0 <= r - i < rows and 0 <= c + i < cols:
                if field[r - i][c + i] == player:
                    sequence_counter += 1
                else:
                    break
        return sequence_counter >= win_condition

    return check_horizontal() or check_vertical() or check_diagonal() or check_reverse_diagonal()


def apply_player_move(player):
    column = player_makes_move(player)
    for row in range(rows - 1, -1, -1):
        if field[row][column] == 0:
            field[row][column] = player
            return row, column


def player_makes_move(player):
    while True:
        try:
            chosen_col = int(input(f"{players[player]}({player}), please pick a column: ")) - 1
        except ValueError:
            print("Column value is invalid. Try again.")
            continue

        if not (0 <= chosen_col < cols):
            print("Column is outside the field. Try again.")
            continue
        elif field[0][chosen_col] != 0:
            print("This column is already full. Try again.")
            continue
        else:
            break

    return chosen_col

print("WELCOME\n"
      "This is Connect 4 Plus. An upgraded and more entertaining version of the popular kid's game Connect Four.\n"
      "Here you can choose the size of the field of play and how many you have to connect to win.\n")

while True:
    rows = int(input("Enter the numbers of rows in the playing field: "))
    cols = int(input("Enter the numbers of columns in the playing field: "))
    if rows <= 0 or cols <=0:
        print("Number of rows and columns cannot be a less than 1. Please enter valid values.")
    else:
        break

while True:
    win_condition = int(input("Pick the win condition for the current game: "))
    if win_condition > rows and win_condition > cols:
        print(f"The win condition is too big for the field. Please pick a number that fits in the field({rows}x{cols})")
    else:
        break

player_1 = input("Pick a name for the player № 1: ")
player_2 = input("Pick a name for the player № 2: ")
players = {1: player_1, 2: player_2}
field = [[0] * cols for _ in range(rows)]
print("Game starting now!")
print(*field, sep="\n")

current_player, next_player = 1, 2

while True:
    move_coordinates = apply_player_move(current_player)
    print(*field, sep="\n")

    if check_win_condition(*move_coordinates):
        print(f"{players[current_player]} won the game!")
        exit()
    elif 0 not in field[0]:
        print("The field is full. Draw.")
        exit()

    current_player, next_player = next_player, current_player
