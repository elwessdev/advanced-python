from random import randint

def display_board(board):
    for row in board:
        print("+---+---+---+")
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print("+---+---+---+")

def is_draw(board):
    return all(i in ["X", "O"] for row in board for i in row)

def victory_for(board, sign):
    for r in board:
        if all(cell == sign for cell in r):
            print(f"{sign} win")
            return True

    for i in range(3):
        if all(board[j][i] == sign for j in range(3)):
            print(f"{sign} win")
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        print(f"{sign} win")
        return True
    return False

def enter_move(board):
    while True:
        try:
            user = int(input("Enter your move: "))
            if user < 1 or user > 9:
                print("Enter your move: ")
                continue
            r, c = (user - 1) // 3, (user - 1) % 3
            if board[r][c] in ["X", "O"]:
                print("ty again.")
                continue
            break
        except ValueError:
            print("please enter a valid number")
    board[r][c] = "O"
    if victory_for(board, "O"):
        return
    if is_draw(board):
        print("draw brooo")
        return
    draw_move(board)

def draw_move(board):
    r, c = randint(0, 2), randint(0, 2)
    while board[r][c] in ["X", "O"]:
        r, c = randint(0, 2), randint(0, 2)

    board[r][c] = "X"
    display_board(board)
    
    if victory_for(board, "X"):
        return
    if is_draw(board):
        print("draw broo")
        return
    enter_move(board)

# Start
boardGlobal = [[3*j + i for i in range(1, 4)] for j in range(3)]
draw_move(boardGlobal)