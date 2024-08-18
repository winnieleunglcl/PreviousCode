def tic_tac_toe_win(board):
    winner = ""
    a = len(board)

    for i in range(a):
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != 0:
            return board[i][0]

        col = set([board[0][i], board[1][i], board[2][i]])
        if len(col) == 1 and board[0][i] != 0:
            return board[0][i]

    diag1 = set([board[0][0], board[1][1], board[2][2]])
    diag2 = set([board[0][2], board[1][1], board[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and board[1][1] != 0:
        return board[1][1]

    return None

     
        

    

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(f"Player {tic_tac_toe_win(winner_is_2)} wins the game")
print(f"Player {tic_tac_toe_win(winner_is_1)} wins the game")
print(f"Player {tic_tac_toe_win(winner_is_also_1)} wins the game")
print(f"Player {tic_tac_toe_win(no_winner)} wins the game")
print(f"Player {tic_tac_toe_win(also_no_winner)} wins the game")
