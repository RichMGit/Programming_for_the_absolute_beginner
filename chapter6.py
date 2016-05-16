# # Keyword Arguments
#
# def fake_function(name = "Jackson", age = 15):
#     print('Happy birthday ', name, ' I hear you are ', age, ' today')
#
# fake_function(age = 55, name = 'Dennis')
#
#

# value = 10
#
# def first_func():
#     print(value)
#
# first_func()

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "--------- ")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "--------- ")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


display_board(board)

print('Lets play')

user_go = int(input('Choose a square to play in: '))


for i,v in enumerate(board):
    if v == user_go:
        board[v]='X'

# board[user_go] = 'X'

board.isDigit(1)

display_board(board)
