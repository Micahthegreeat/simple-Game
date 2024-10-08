#Miach Knox10/7/24
#a game about making products


import time
import random
import display
#defining starting variables
grid_size = 5
#dictionary with every board size


board = {}
for x in range(2,13):
    board[f"board{x}"] = [[['','',''] for j in range(x) ] for i in range(x)]
    #example board for visualization
# [
# [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
# [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
# [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
# [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
# [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
# ]

def main():
    
    display.board(board['board2'])

if __name__ == '__main__':
    main()