import random


def print_positions_board():
	print(' 9 | 8 | 7 |')
	print(' 4 | 5 | 6 |')
	print(' 1 | 2 | 3 |')

def display_board(board):
	print("\n" * 100)
	print(f' {board[9]} | {board[8]} | {board[7]} |')
	print(f' {board[4]} | {board[5]} | {board[6]} |')
	print(f' {board[1]} | {board[2]} | {board[3]} |')
	print("\n")

def player_input():
	marker = ''
	while marker not in ['X', 'O']:
		marker = input("\nWhat do you want to choose 'X' or 'O' ? ").upper()
	if marker == 'X':
		return 'X', '0'
	else:
		return 'O', 'X'


def choose_first():
	return random.choice(['Player 1', 'Player 2'])


def place_marker(board, marker, position):
	board[position] = marker[0]
	return board


def win_check(board, mark):
	return ((board[1] == board[2] == board[3] == mark) or
			(board[4] == board[5] == board[6] == mark) or
			(board[7] == board[8] == board[9] == mark) or
			(board[9] == board[5] == board[3] == mark) or
			(board[7] == board[5] == board[1] == mark) or
			(board[9] == board[4] == board[1] == mark) or
			(board[8] == board[5] == board[2] == mark) or
			(board[7] == board[6] == board[3] == mark))


def space_check(board, position):
	return board[position] == ' '


def full_board_check(board):
	return ' ' not in board


def player_choice(board, player):
	position = 0
	while True:
		try:
			position = int(input(f"{player}, choose your next position : (1-9) : "))
		except ValueError:
			print('Please enter a valid input')
		else:
			if position not in range(1, 10) or not space_check(board, position):
				print('Please choose an available position.')
			else:
				break
	return position


def replay():
	return input("Do you want to play again? (Yes, No) : ").lower().startswith('y')


def tic_tac_toe_game():
	print('Welcome to Tic Tac Toe!\n')
	print_positions_board()
	while True:
		game_board = [' '] * 10
		player1_marker, player2_marker = player_input()
		turn = choose_first()
		print(f'{turn} will go first ')
		play_game = input("\nAre you ready to play the game? (Yes, No) : ").lower()
		if play_game == 'yes' or play_game == 'y':
			game_on = True
		else:
			game_on = False
		while game_on:
			if turn == 'Player1':
				display_board(game_board)
				position = player_choice(game_board, "Player 1")
				place_marker(game_board, player1_marker, position)
				if win_check(game_board, player1_marker):
					display_board(game_board)
					print("\nCongratulations !! You won the game !!")
					game_on = False
				else:
					if full_board_check(game_board):
						display_board(game_board)
						print("\nThe game is a draw !!")
						break
					else:
						turn = 'Player2'
			else:
				display_board(game_board)
				position = player_choice(game_board, "Player 2")
				place_marker(game_board, player2_marker, position)
				if win_check(game_board, player2_marker):
					display_board(game_board)
					print("\nPlayer 2 won the game !!")
					game_on = False
				else:
					if full_board_check(game_board):
						display_board(game_board)
						print("\nThe game is a draw !!")
						break
					else:
						turn = 'Player1'
		
		if not replay():
			break


tic_tac_toe_game()
