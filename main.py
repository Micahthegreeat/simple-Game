#Miach Knox10/7/24
#a game about making products


import time
import random
import display
#defining starting variables
grid_size = 5
board = [
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
    ]

def main():
    
    display.board(grid_size, board)

if __name__ == '__main__':
    main()